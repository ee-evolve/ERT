package extractor

import (
    "strings"
    "testing"
)

func TestExtractor(t *testing.T) {
    got := parseLines(strings.NewReader("jenkins\nterraform\n"))
    want := []string{"jenkins", "terraform"}

    for i := 0; i < 2; i++ {
        if got[i] != want[i] {
            t.Errorf("got: %s, want: %s", got[i], want[i])
        }
    }
}