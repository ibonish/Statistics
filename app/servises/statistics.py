import numpy as np


def get_data_statistics(data: list) -> dict:
    return {
        'минимальное значение': np.min(data),
        'максимальное значение': np.max(data),
        'количество': len(data),
        'сумма': np.sum(data),
        'медиана': np.median(data),
    }
