package main

import (
  "fmt"
  "net/http"
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

