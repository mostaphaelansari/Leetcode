package main

import (
	"fmt"
	"strings"
)

func stringMatching(words []string) []string {
	result := []string{}

	// Iterate over each word
	for i := 0; i < len(words); i++ {
		for j := 0; j < len(words); j++ {
			// Check if words[i] is a substring of words[j] and ensure i != j
			if i != j && strings.Contains(words[j], words[i]) {
				result = append(result, words[i])
				break // Avoid duplicates
			}
		}
	}

	return result
}
