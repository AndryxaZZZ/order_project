def check_total_cost(input_data: int) -> float:
    """
    Рассчитывает общую стоимость заказа скрепок
    
    Args:
        input_data (int): количество скрепок
        
    Returns:
        float: общая стоимость заказа
        
    Правила расчета:
    - 0 шт: 0 руб
    - 1-100 шт: 10 руб/шт
    - 101-200 шт: 9 руб/шт
    - 201-300 шт: 8 руб/шт
    - свыше 300 шт: 7 руб/шт
    """
    if input_data == 0:
        return 0.0
    
    if 1 <= input_data <= 100:
        return input_data * 10.0
    elif 101 <= input_data <= 200:
        return input_data * 9.0
    elif 201 <= input_data <= 300:
        return input_data * 8.0
    else:
        return input_data * 7.0