import pytest

from app.utils.check_data import check_total_cost

class TestCheckTotalCost:
    """Тестирование функции расчета общей стоимости заказа"""
    
    def test_zero_quantity(self):
        """Тест для 0 скрепок - должна быть 0 стоимость"""
        assert check_total_cost(0) == 0.0
    
    def test_lower_bound_class1(self):
        """Тест нижней границы класса 1 (1 скрепка)"""
        assert check_total_cost(1) == 10.0
    
    def test_upper_bound_class1(self):
        """Тест верхней границы класса 1 (100 скрепок)"""
        assert check_total_cost(100) == 1000.0
    
    def test_middle_class1(self):
        """Тест середины класса 1 (50 скрепок)"""
        assert check_total_cost(50) == 500.0
    
    def test_lower_bound_class2(self):
        """Тест нижней границы класса 2 (101 скрепка)"""
        assert check_total_cost(101) == 909.0
    
    def test_upper_bound_class2(self):
        """Тест верхней границы класса 2 (200 скрепок)"""
        assert check_total_cost(200) == 1800.0
    
    def test_middle_class2(self):
        """Тест середины класса 2 (150 скрепок)"""
        assert check_total_cost(150) == 1350.0
    
    def test_lower_bound_class3(self):
        """Тест нижней границы класса 3 (201 скрепка)"""
        assert check_total_cost(201) == 1608.0
    
    def test_upper_bound_class3(self):
        """Тест верхней границы класса 3 (300 скрепок)"""
        assert check_total_cost(300) == 2400.0
    
    def test_middle_class3(self):
        """Тест середины класса 3 (250 скрепок)"""
        assert check_total_cost(250) == 2000.0
    
    def test_lower_bound_class4(self):
        """Тест нижней границы класса 4 (301 скрепка)"""
        assert check_total_cost(301) == 2107.0
    
    def test_middle_class4(self):
        """Тест середины класса 4 (400 скрепок)"""
        assert check_total_cost(400) == 2800.0
    
    def test_large_quantity(self):
        """Тест для большого количества (1000 скрепок)"""
        assert check_total_cost(1000) == 7000.0