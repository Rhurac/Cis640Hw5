import impl
from impl import Queue
import hypothesis.strategies as st
from hypothesis import given


# noinspection PyBroadException
class TestQueue:
    """ Tests for the properties of a Queue """

    # A strategy which generates only valid inputs that can be queued
    strat_valid_input = st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False) | st.text() | st.integers() | st.booleans()))

    @given(strat_valid_input)
    def test_popped_item_was_first_item_pushed(self, lst):
        """ If len() > 0 and x = pop(), then x was the first item pushed and remove x from Queue """
        try:
            q = Queue()
            for x in lst:
                q.enqueue(x)
            while q.len() > 1:
                q.dequeue()
            if len(lst) > 0:
                assert q.dequeue() is lst[0]
        except:
            assert False

    @given(strat_valid_input)
    def test_empty_queue_is_length_zero(self, lst):
        """ If nothing has been placed on the queue, then length is zero """
        try:
            q = Queue()
            for x in lst:
                q.enqueue(x)
            while q.len() > 0:
                q.dequeue()
            assert q.len() == 0
        except:
            assert False

    @given(strat_valid_input)
    def test_pop_decrements_count(self, lst):
        """ Calls to a successful pop should decrement the length by one """
        try:
            q = Queue()
            for x in lst:
                q.enqueue(x)
            for i in range(1, len(lst)):
                q.dequeue()
                assert q.len() == len(lst) - i
        except:
            assert False

    @given(strat_valid_input)
    def test_push_increments_count(self, lst):
        """ Calls to successful push should increment the length by one """
        pass

    @given(strat_valid_input)
    def test_pop_empty_queue_returns_none(self, lst):
        """ Popping an empty queue should return None """
        try:
            q = Queue()
            for x in lst:
                q.enqueue(x)
            while q.len() > 0:
                q.dequeue()
            assert q.dequeue() is None
        except:
            assert False

    def test_push_none_raises_exception(self):
        """ Pushing value None raises a ValueError exception """
        try:
            q = Queue()
            q.enqueue(None)
            assert False
        except ValueError:
            assert True
        except:
            assert False

    @given(strat_valid_input)
    def test_popping_empty_queue_does_not_change_length(self, lst):
        """ Popping and empty queue does not change the length """
        try:
            q = Queue()
            cnt = len(lst)
            for x in lst:
                q.enqueue(x)
            while q.len() > 0:
                q.dequeue()
            assert q.len() == 0
            q.dequeue()
            assert q.len() == 0
        except:
            assert False

    @given(strat_valid_input)
    def test_popping_nonempty_queue_does_not_return_none(self, lst):
        """ Popping a queue with length greater than zero returns an object """
        try:
            q = Queue()
            for x in lst:
                q.enqueue(x)
            while q.len() > 0:
                assert q.dequeue() is not None
        except:
            assert False

    @given(st.lists(min_size=1, elements=(st.floats(allow_nan=False, allow_infinity=False) | st.text() | st.integers() | st.booleans())))
    def test_length_of_queue(self, lst):
        """ The length of the queue should be equal to number of pushes minus pops """
        try:
            q = Queue()
            pushes = 0
            pops = 0
            for x in lst:
                q.enqueue(x)
                pushes = pushes + 1
                assert q.len() == pushes - pops
            while q.len() > 0:
                q.dequeue()
                pops = pops + 1
                assert q.len() == pushes - pops
        except:
            assert False



