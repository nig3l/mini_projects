package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func currencyConverter(amount float64, fromCurrency string, toCurrency string) float64 {
	// Get the exchange rate from the Open Exchange Rates API.
	url := "https://api.exchangeratesapi.io/latest?base=" + fromCurrency
	resp, err := http.Get(url)
	if err != nil {
	  panic(err)
	}

	defer resp.Body.Close()

  data, err := resp.ReadAll()
  if err != nil {
    panic(err)
  }

  exchangeRate := rates[toCurrency]

    // Convert the amount.
	convertedAmount := amount * exchangeRate

	return convertedAmount
  }

  func main() {
	amount := 100
	fromCurrency := "USD"
	toCurrency := "EUR"
	convertedAmount := currencyConverter(amount, fromCurrency, toCurrency)
	fmt.Printf("%.2f %s is equal to %.2f %s\n", amount, fromCurrency, convertedAmount, toCurrency)
  }

  



