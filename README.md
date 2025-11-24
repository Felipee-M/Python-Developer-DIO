# Simple Bank (CLI) — Python · v2 (OOP & Abstractions)

A simple and instructional banking system in Python, now rewritten with **Object-Oriented Programming**.  
This version introduces **classes**, **abstract base classes (ABCs)**, and clearer separation of concerns while keeping the same terminal experience.

## What’s new in v2
- ✅ Refactored to **OOP** (classes for account, operations, and app flow).
- ✅ **Abstract base classes** to define contracts for operations/services.
- ✅ Clearer **responsibility boundaries** (I/O vs. domain logic).
- ✅ Easier to extend (e.g., add daily withdrawal limits, fees, or new account types).

## Features (unchanged behavior, better design)
- **Deposit**: adds positive amounts to the balance and records the transaction.
- **Withdraw**: deducts from the balance (with validations for sufficient funds and positive amount).
- **Statement**: lists all transactions (deposits/withdrawals) and shows the current balance.
- **Interactive menu**: simple navigation through options in the terminal.
