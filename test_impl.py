import impl
from impl import Queue
import hypothesis.strategies as st
from hypothesis import given


class TestQueue:
    """ Tests for the properties of a Queue """

    # A strategy which generates only valid inputs that can be queued
    strategy = st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False) | st.text() | st.integers() | st.booleans()))

    @given(strategy)
    def test_popped_item_was_first_item_pushed(self, x):
        """ If len() > 0 and x = pop(), then x was the first item pushed and remove x from Queue """
        pass

    def test_empty_queue_is_length_zero(self):
        """ If nothing has been placed on the queue, then len() = 0 """
        pass

    def test_pop_decrements_count(self):
        """ Calls to a successful pop should decrement the length by one """
        pass

    def test_push_increments_count(self):
        """ Calls to successful push should increment the length by one """
        pass

    def test_pop_empty_queue_returns_none(self):
        """ Popping an empty queue should return None """
        pass

    def test_push_none_raises_exception(self):
        """ Pushing value None raises a ValueError exception """
        pass

    def test_popping_empty_queue_does_not_change_length(self):
        """ Popping and empty queue does not change the length """
        pass

    def test_popping_nonempty_queue_does_not_return_none(self):
        """ Popping a queue with length greater than zero returns an object """
        pass

    def test_length_of_queue(self):
        """ The length of the queue should be equal to number of pushes minus pops """
        pass


