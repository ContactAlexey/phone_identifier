<body>
  <h1>🌍 International Phone Prefix Identifier 📞</h1>

  <p>A simple and user-friendly Python GUI tool built with <code>tkinter</code> to identify the <strong>country or region</strong> from an international phone number prefix.</p>

  <h2>🚀 Features</h2>
  <ul>
    <li>🗺️ Supports hundreds of international dialing codes</li>
    <li>🧠 Smart detection of shared prefixes like <code>+1</code> (USA, Canada, Caribbean) and <code>+7</code> (Russia, Kazakhstan)</li>
    <li>🧪 Validates input format (must start with <code>+</code>)</li>
    <li>🖥️ Clean and minimal graphical interface</li>
  </ul>

  <h2>🛠️ How to Use</h2>
  <ol>
    <li><strong>Run the script</strong><br>The GUI window will appear.</li>
    <li><strong>Enter a phone number</strong><br>Format: <code>+</code> followed by the full number (e.g. <code>+14165550123</code>).</li>
    <li><strong>Click "Identify Country"</strong><br>The app will display the corresponding <strong>country name</strong> or region.</li>
  </ol>

  <h2>🧾 Example</h2>
  <p><strong>Input:</strong><br><code>+14165550123</code></p>
  <p><strong>Output:</strong><br><code>Result: Canada 🇨🇦</code></p>

  <h2>🧱 Built With</h2>
  <ul>
    <li>🐍 Python 3</li>
    <li>🎨 Tkinter (for GUI)</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre><code>phone_identifier.py  # Main script</code></pre>

  <h2>⚠️ Notes</h2>
  <ul>
    <li>If the number starts with a known prefix but lacks a valid subcode, you'll get a partial match message.</li>
    <li>The dataset includes most countries and key subregions sharing country codes.</li>
  </ul>

  <h2>📸 GUI Preview</h2>
  <pre>
+-------------------------------+
|  Enter phone number:         |
|  [ +14165550123           ]  |
|                               |
|     [ Identify Country ]     |
|                               |
|      Result: Canada           |
+-------------------------------+
  </pre>

  <h2>📃 License</h2>
  <p>This project is free to use and modify for personal or educational purposes.</p>
</body>
