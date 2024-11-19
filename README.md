### Temperature Converter Program

This Python program allows users to convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin** scales. Users input a temperature value along with its original unit, and the program calculates and displays the equivalent values in the other two units.

---

### Features

- **User-friendly Input:** 
  - Users can enter the temperature value and specify the unit of measurement (C, F, or K).
- **Accurate Conversions:** 
  - The program uses standard conversion formulas for precise results.
- **Formatted Output:** 
  - Results are displayed up to two decimal places for better readability.
- **Error Handling:** 
  - Displays a message for invalid unit inputs.

---

### How It Works

1. **Input:**
   - The program prompts the user to enter a temperature value (e.g., `25`) and its unit of measurement:
     - `C` for Celsius
     - `F` for Fahrenheit
     - `K` for Kelvin

2. **Processing:**
   - Based on the input unit, the program converts the temperature to the other two units using these formulas:
     - **Celsius to Fahrenheit:** \( F = C \times \frac{9}{5} + 32 \)
     - **Celsius to Kelvin:** \( K = C + 273.15 \)
     - **Fahrenheit to Celsius:** \( C = (F - 32) \times \frac{5}{9} \)
     - **Kelvin to Celsius:** \( C = K - 273.15 \)

3. **Output:**
   - Displays the original temperature along with its converted values in the other two units.


### How to Run the Program

1. Clone this repository to your local machine.
2. Open the terminal and navigate to the project directory.
3. Run the program using Python:
   ```bash
   python temperature_converter.py
   ```
4. Follow the prompts to enter the temperature and unit.

---

### Future Enhancements

- Add support for batch conversions.
- Implement a graphical user interface (GUI).
- Provide additional temperature scales like Rankine.

---

### License

This project is open-source and available under the **MIT License**. Feel free to modify and share! 😊

--- 

### Contribution

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request. 
