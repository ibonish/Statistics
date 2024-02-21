import numpy as np
from fastapi import HTTPException


def get_data_statistics(data: list) -> dict:
    if not data:
        raise HTTPException(
            status_code=400,
            detail='Данных за данный период нет',
        )
    return {
        'минимальное значение': np.min(data),
        'максимальное значение': np.max(data),
        'количество': len(data),
        'сумма': np.sum(data),
        'медиана': np.median(data),
    }
