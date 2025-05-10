"""
Script to run the entire analysis process.
"""
import os
import subprocess
import time

def run_command(command):
    """Run a command and print its output."""
    print(f"\n=== Running: {command} ===")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    # Print output in real-time
    for line in iter(process.stdout.readline, b''):
        print(line.decode('utf-8'), end='')
    
    process.wait()
    return process.returncode

def main():
    """Run the entire analysis process."""
    # Step 1: Generate random solutions
    print("\n=== Step 1: Generating random solutions ===")
    if run_command("python generate_random_solutions.py") != 0:
        print("Error generating random solutions. Exiting.")
        return
    
    # Step 2: Analyze solutions
    print("\n=== Step 2: Analyzing solutions ===")
    if run_command("python analyze_random_solutions.py") != 0:
        print("Error analyzing solutions. Exiting.")
        return
    
    # Step 3: Visualize results
    print("\n=== Step 3: Visualizing results ===")
    if run_command("python visualize_results.py") != 0:
        print("Error visualizing results. Exiting.")
        return
    
    # Step 4: Open the HTML report
    print("\n=== Step 4: Opening HTML report ===")
    if os.path.exists("assessment_analysis_report.html"):
        if run_command("python -m webbrowser assessment_analysis_report.html") != 0:
            print("Error opening HTML report. Please open it manually.")
    else:
        print("HTML report not found. Please check the previous steps for errors.")
    
    print("\n=== Analysis complete! ===")
    print("Results are available in:")
    print("- analysis_results.csv: Raw analysis data")
    print("- ranked_candidates.json: Ranked candidates data")
    print("- charts/: Visualization charts")
    print("- assessment_analysis_report.html: HTML report with all charts")

if __name__ == "__main__":
    main()
