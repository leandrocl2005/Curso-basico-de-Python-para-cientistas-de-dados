from typing import Callable

import pandas as pd
from sktime.transformations.series.boxcox import LogTransformer
from sktime.transformations.series.detrend import Deseasonalizer, Detrender


def preprocessing_date(
    data: pd.DataFrame, period: str, date_column_name: str = "Date"
) -> pd.DataFrame:
    """Return data with Date feature in index.

    Args:
        data (pd.DataFrame): Data with a "Date" column
        period (str): "D", "M", "Y"
        date_column_name (str): Default is "Date"
    """
    data_copy = data.copy()
    data_copy[date_column_name] = pd.to_datetime(data_copy[date_column_name])
    data_copy[date_column_name] = data_copy[date_column_name].dt.to_period(period)
    data_copy.set_index(date_column_name, inplace=True)
    return data_copy


def make_transformations(
    y: pd.Series,
) -> tuple[pd.Series, Callable[[pd.Series], pd.Series]]:
    """Make usual transformations on serie

    Args:
        y (pd.Series): A serie in a sktime format.

    Returns:
        tuple[pd.Series, Callable[[pd.Series], pd.Series]]: A transformed serie
        and a function to invert the transformation
    """
    y_copy = y.copy()
    y_mean = y.mean()
    y_std = y.std()
    log_transform = LogTransformer()
    trend_transform = Detrender()
    deseason_transform = Deseasonalizer()
    y_copy = log_transform.fit_transform(y_copy)
    y_copy = trend_transform.fit_transform(y_copy)
    y_copy = deseason_transform.fit_transform(y_copy)
    y_copy = (y_copy - y_mean) / y_std

    def inverse_transformation(serie):
        serie_copy = serie.copy()
        serie_copy = serie_copy * y_std + y_mean
        serie_copy = deseason_transform.inverse_transform(serie_copy)
        serie_copy = trend_transform.inverse_transform(serie_copy)
        serie_copy = log_transform.inverse_transform(serie_copy)
        return serie_copy

    return y_copy, inverse_transformation
