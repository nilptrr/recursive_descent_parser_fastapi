from fastapi import FastAPI
from typing import Optional
import uvicorn

from rdp.calculator import calculate
from expr_storage import ExpessionStorage
from schemas import ExpressionResult


expression_storage = ExpessionStorage()

app = FastAPI()


@app.get('/calc/{expr}', response_model=ExpressionResult)
def calc(expr: str):
    """Calculates the value of the expression.

    Args:
        expr (str): _description_

    Returns:
        _type_: _description_
    """
    try:
        expr_result = calculate(expr)

    except Exception:
        expr_result = ''
        status = 'fail'

    else:
        status = 'success'

    finally:
        expr_out = ExpressionResult(
            request = expr,
            response = expr_result,
            status = status
        )
        
        expression_storage.add_item(expr_out)
        return expr_out


@app.get('/history')
def history(limit: Optional[str] = 30, status: Optional[str] = None):
    """Get the calculation history.

    Args:
        limit (int, optional): _description_. Defaults to 30.
        status (Optional[str], optional): _description_. Defaults to None.
    """
    try:
        result = expression_storage.get_items(int(limit), status)

    except Exception as e:
        return e.args[0]

    else:
        return result


def run_api():
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)


if __name__ == '__main__':
    run_api()
