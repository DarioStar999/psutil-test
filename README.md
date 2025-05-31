<h1>System Monitor CLI Tool</h1>

<p>This is a simple command-line interface (CLI) tool built with <strong>Python</strong> and <code>psutil</code> that allows you to monitor your system’s resource usage and manage processes.</p>

<h2>Features</h2>
<ul>
  <li>Display current CPU usage percentage</li>
  <li>Show memory usage percentage</li>
  <li>Check disk usage of the root directory</li>
  <li>List all running processes with their PID, CPU, and memory usage</li>
  <li>Find the PID of a process by its name</li>
</ul>

<h2>Usage</h2>
<p>Run the script and choose from the menu options:</p>
<ol>
  <li>CPU Usage</li>
  <li>Memory Usage</li>
  <li>Disk Usage</li>
  <li>Process List</li>
  <li>Get PID of a specific process</li>
  <li>Exit the tool</li>
</ol>

<h2>Requirements</h2>
<ul>
  <li><code>psutil</code> library: install with <code>pip install psutil</code></li>
  <li>Python 3.x</li>
</ul>

<h2>Example</h2>
<pre><code>
Choose an option:
1) CPU Usage
2) Memory Usage
3) Disk Usage
4) Process List
5) Process Pid
6) Exit
Choice: 1
CPU Usage: 23.5%
  
</code></pre>

<h2>Note</h2>
<p>This tool runs in an infinite loop until you choose to exit. Make sure to run it in a terminal or command prompt that supports interactive input.</p>
