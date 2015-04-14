from sequencer_editor import *
import unittest

def get_editor():
    root = Tkinter.Tk()
    sample_names = [str(i) for i in range(8)]
    return SequencerEditor(root, 8, sample_names, 120.0)

class Tests(unittest.TestCase):


    def test_button_grid_increase_number_beats(self):
        editor = get_editor()
        button_grid = editor.button_grid
        button_grid.set_number_beats(10)
        self.assertTrue(button_grid.number_beats == 10)
        self.assertTrue(len(button_grid.buttons) == 10)
        for beat in range(10):
            for sample in range(8):
                position = (beat, sample)
                self.assertFalse(button_grid.buttons[beat][sample].state)
                self.assertTrue(button_grid.buttons[beat][sample].position == position)

    def test_button_grid_decrease_number_beats(self):
        editor = get_editor()
        button_grid = editor.button_grid
        button_grid.set_number_beats(4)
        self.assertTrue(button_grid.number_beats == 4)
        self.assertTrue(len(button_grid.buttons) == 4)
        for beat in range(4):
            for sample in range(8):
                position = (beat, sample)
                self.assertFalse(button_grid.buttons[beat][sample].state)
                self.assertTrue(button_grid.buttons[beat][sample].position == position)

    def test_button_grid_set_number_beats_keep_states(self):
        editor = get_editor()
        for sample in range(4, 8):
            editor.set_button_state((0, sample), True)
        button_grid = editor.button_grid
        button_grid.set_number_beats(4)
        self.assertTrue(button_grid.number_beats == 4)
        self.assertTrue(len(button_grid.buttons) == 4)
        beat0 = [button.state for button in button_grid.buttons[0]]
        self.assertEquals(set([False]), set(beat0[0:4]))
        self.assertEquals(set([True]), set(beat0[4:]))

        for beat in range(1, 4):
            for sample in range(8):
                position = (beat, sample)
                self.assertFalse(button_grid.buttons[beat][sample].state)
                self.assertTrue(button_grid.buttons[beat][sample].position == position)



if __name__ == '__main__':
    unittest.main()