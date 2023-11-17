package main

import (
	"fmt"
	"os"
)

func getExceptValue(number int) string {
	switch number {
	case 90:
		return "XC"
	case 100:
		return "C"
	case 40:
		return "XL"
	}
	return ""
}

func checkRomanNumerals(romanNumeral string) string {
	for key, _ := range romanNumbers {
		if key == romanNumeral {
			return romanNumeral
		}
	}
	return ""
}

func calcRomExpression(firstOperand string, lastOperand string, operate string) string {
	fOperand := convertRomanToInteger(firstOperand)
	lOperand := convertRomanToInteger(lastOperand)

	if fOperand < lOperand && operate == "-" {
		fmt.Println("The Roman system does not have negative numbers")
		os.Exit(1)
	}

	switch operate {
	case "+":
		return convertIntegerToRoman(fOperand + lOperand)
	case "-":
		return convertIntegerToRoman(fOperand - lOperand)
	case "*":
		return convertIntegerToRoman(fOperand * lOperand)
	case "/":
		return convertIntegerToRoman(fOperand / lOperand)
	}
	return ""
}

func convertRomanToInteger(romanNumeral string) int {
	number := 0
	if romanNumeral == "IV" {
		return 4
	}
	if romanNumeral == "IX" {
		return 9
	}

	for _, char := range []rune(romanNumeral) {
		number += digits[string(char)]
	}
	return number
}

func convertIntegerToRoman(number int) string {
	except := getExceptValue(number)
	if except != "" {
		return except
	}

	str := ""
	numberOfTens := number / 10
	remainder := number % 10

	for i := 0; i < numberOfTens; i++ {
		str += "X"
	}
	for key, value := range romanNumbers {
		if value == remainder {
			str += key
		}
	}

	if 50 <= number {
		highestRank := "L" + str[5:]
		return highestRank
	}
	return str
}

func calcToRomanSys(firstOperand string, lastOperand string, operate string) {
	fOperand := checkRomanNumerals(firstOperand)
	lOperand := checkRomanNumerals(lastOperand)

	if fOperand != "" && lOperand != "" {
		result := calcRomExpression(fOperand, lOperand, operate)
		if result == "" {
			fmt.Println("Unsupported operator")
			os.Exit(1)
		}
		fmt.Println(result)
	} else {
		fmt.Println("The expression does not contain Roman numerals")
		os.Exit(1)
	}
}
