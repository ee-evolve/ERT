package extractor

import (
    "bufio"
    "io"
    "os"
)

func Extract(filename string) []string {
    f, err := os.Open(filename)
    defer f.Close()

    if err != nil {
        panic("Could not open file")
    }

    return parseLines(f)
}

func parseLines(file io.Reader) []string {
    scanner := bufio.NewScanner(file)
    arr := make([]string, 0)

    for scanner.Scan() {
        line := scanner.Text()
        arr = append(arr, line)
    }

    return arr
}

