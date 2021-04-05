from unittest import TestCase

from array_list import ArrayList


class TestArrayList(TestCase):
    def setUp(self):
        self.al = ArrayList()

    def test_append__when_list_is_empty__should_add_to_then_end(self):
        self.al.append(1)
        values = list(self.al)

        self.assertEqual([1], values)

    def test_append__to_return(self):
        result = self.al.append(1)

        self.assertEqual(self.al, result)

    def test_append__when_list_is_not_empty__should_add_to_then_end(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(3)
        values = list(self.al)

        self.assertEqual([1, 2, 3], values)

    def test_append__1024_values_expect_append__to_the_end(self):
        values = [x for x in range(1024)]
        [self.al.append(x) for x in values]
        list_values = list(self.al)

        self.assertEqual(values, list_values)

    def test_remove__when_index_is_valid__expect_remove_values_and_return_it(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(33)
        self.al.append(4)

        result = self.al.remove(2)
        self.assertEqual([1, 2, 4], list(self.al))
        self.assertEqual(33, result)

    def test_remove__when_index_is_invalid__expect_remove_values_and_raise(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(3)
        self.al.append(4)

        with self.assertRaises(IndexError):
            self.al.remove(self.al.size())

    def test_get__when_index_is_valid__expect_remove_values_and_return_it(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(33)
        self.al.append(4)

        result = self.al.get(2)
        self.assertEqual(33, result)

    def test_get__when_index_is_invalid__expect_remove_values_and_raise(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(3)
        self.al.append(4)

        with self.assertRaises(IndexError):
            self.al.get(self.al.size())

    def test_extend_with_empty_iterable_expect_to_be_same(self):
        self.al.append(1)

        self.al.extend([])
        self.assertEqual([1], list(self.al))

    def test_extend__when_empty_with_not_empty_iterable__expect_to_be_same(self):
        self.al.extend([1])
        self.assertEqual([1], list(self.al))

    def test_extend_with_ist_expect_to_append_the_list(self):
        self.al.append(1)

        self.al.extend([2])
        self.assertEqual([1, 2], list(self.al))

    def test_extend_with_generator_expect_to_append_the_list(self):
        self.al.append(1)

        self.al.extend([x for x in range(1)])
        self.assertEqual([1, 0], list(self.al))

    def test_extend__with_not_iterable_expect_to_raise_valueError(self):
        self.al.append(1)

        with self.assertRaises(ValueError):
            self.al.extend(2)

    def test_insert__when_index_is_valid__expect_insert_values_at_index(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(4)
        self.al.append(5)
        self.al.append(6)
        self.al.append(7)
        self.al.append(8)
        self.al.append(9)

        self.al.insert(2, 33)
        self.assertEqual([1, 2, 33, 4, 5, 6, 7, 8, 9], list(self.al))

    def test_insert__when_index_is_invalid__expect_insert_values_and_raise(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(4)

        with self.assertRaises(IndexError):
            self.al.insert(self.al.size() + 1, 2)

    def test_pop__expect_to_remove_last_element_and_remove_it(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(3)
        self.al.append(4)

        result = self.al.pop()

        self.assertEqual(4, result)
        self.assertListEqual([1, 2, 3], list(self.al))

    def test_pop__when_empty_expect_raise(self):
        with self.assertRaises(IndexError):
            self.al.pop()

    def test_clear_expect_to_be_empy(self):
        [self.al.append(x) for x in range(15)]
        self.al.clear()

        self.assertEqual([], list(self.al))

    def test_index__when_item_is_present__expect_to_return_correct_index(self):
        [self.al.append(x) for x in range(15)]

        index = self.al.index(5)
        self.assertEqual(5, index)

    def test_index__when_item_is_not_present__expect_to_raise(self):
        [self.al.append(x) for x in range(15)]

        with self.assertRaises(ValueError):
            self.al.index(17)

    def test_count__when_item_is_present__one_time_expect_to_return_1(self):
        [self.al.append(x) for x in range(15)]

        expected_count = 1
        actual_count = self.al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_count__when_item_is_not_present__one_time_expect_to_return_0(self):
        [self.al.append(x) for x in range(15)]

        expected_count = 0
        actual_count = self.al.count(55)
        self.assertEqual(expected_count, actual_count)

    def test_count__when_item_is_present__multiple_times_expect_to_return_correct_count(self):
        [self.al.append(x) for x in range(15)]
        self.al.append(5)
        self.al.insert(3, 5)
        self.al.insert(7, 5)
        self.al.insert(1, 5)
        self.al.insert(9, 5)

        expected_count = 6
        actual_count = self.al.count(5)
        self.assertEqual(expected_count, actual_count)
    def test_count__when_item_is_present__multiple_times_and_once_poped_expect_to_return_correct_count(self):
        [self.al.append(x) for x in range(15)]
        self.al.insert(3, 5)
        self.al.insert(7, 5)
        self.al.insert(1, 5)
        self.al.insert(9, 5)
        self.al.append(5)
        self.al.pop()

        expected_count = 5
        actual_count = self.al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_reverse__expect_in_reversed_order(self):
        [self.al.append(x) for x in range(5)]

        expected = [x for x in range(4, -1, -1)]
        actual = self.al.revers()

        self.assertEqual(expected,actual)

    def test_copy__expect_in_return_an_other_list_with_same_values(self):
        [self.al.append(x) for x in range(5)]

        copied_list = self.al.copy()
        expected_result = [x for x in range(5)]
        actual_result = list(copied_list)

        self.assertNotEqual(copied_list,self.al)
        self.assertEqual(expected_result, actual_result)

    def test_add_first__when_empty__expect_to_add(self):
        self.al.add_first(1)

        self.assertEqual([1], list(self.al))

    def test_add_first__when_not_empty__expect_to_add(self):
        [self.al.append(x) for x in range(5)]

        self.al.add_first(1)

        self.assertEqual([1,0, 1, 2, 3, 4], list(self.al))

    def test_dictionize__when_empty__expect_empty_dict(self):
        actual = self.al.dictionize()
        expected = {}
        self.assertDictEqual(expected, actual)

    def test_dictionize__when_even_element_count__expect_empty_dict(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(3)
        self.al.append(4)

        actual = self.al.dictionize()
        expected = {
            1: 2,
            3: 4
        }
        self.assertDictEqual(expected, actual)

    def test_dictionize__when_odd_element_count__expect_empty_dict(self):
        self.al.append(1)
        self.al.append(2)
        self.al.append(3)
        self.al.append(4)
        self.al.append(5)

        actual = self.al.dictionize()
        expected = {
            1: 2,
            3: 4,
            5: " "
        }
        self.assertDictEqual(expected, actual)