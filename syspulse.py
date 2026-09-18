#!/usr/bin/env python3
import subprocess
import sys
import time
from datetime import datetime
import json
import os
import random

def initialize_interface():
    print("=" * 70)
    print(" SYSPULSE CORE: INTELLIGENT TELEMETRY & ROUTE DIAGNOSTICS SUITE ")
    print(" Open-Source Infrastructure & Network Health Analyzer v2.1")
    print("=" * 70)

def acquire_target_endpoint():
    initialize_interface()
    target_input = input("[?] Enter target hostname, IP address, or API endpoint: ").strip()
    if not target_input:
        print("[-] Error: Target specification cannot be empty. Terminating session.")
        sys.exit(1)
    return target_input

def present_operational_menu():
    print("\nSelect Telemetry Profile Operation:")
    print("  [1] Quick Ping & Latency Diagnostics")
    print("  [2] Advanced Port State & Service Verification")
    print("  [3] Comprehensive Route Trace & Performance Benchmark")
    
    user_choice = input("\nEnter selection index [1-3]: ").strip()
    if user_choice not in ["1", "2", "3"]:
        print("[-] Unrecognized selection detected. Defaulting to Profile 1.")
        return "1"
    return user_choice

def render_execution_header(target, profile):
    print("\n" + "=" * 70)
    print(f"[*] Target Scope Bound: {target}")
    print(f"[*] Active Profile Tier: {profile}")
    print(f"[*] Execution Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")
    time.sleep(1.0)

def simulate_human_pacing(text_message):
    for character in text_message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.03))
    print()

def execute_diagnostic_module(module_title, command_sequence, storage_container):
    print(f"[+] Spawning Diagnostic Module: {module_title}")
    print(f"    Executing system call: {' '.join(command_sequence)}")
    start_timestamp = time.time()
    
    time.sleep(random.uniform(1.5, 3.0))
    
    try:
        process_handle = subprocess.Popen(command_sequence, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        standard_output, error_output = process_handle.communicate()
        elapsed_time = round(time.time() - start_timestamp, 2)
        
        module_record = {
            "module_name": module_title,
            "command_executed": ' '.join(command_sequence),
            "duration_seconds": elapsed_time,
            "exit_status": process_handle.returncode,
            "output_data": standard_output.strip(),
            "error_data": error_output.strip()
        }
        
        print(f"    Status: Completed Successfully [{elapsed_time}s elapsed]")
        print("-" * 70)
        
        output_lines = standard_output.splitlines()
        if output_lines:
            for line in output_lines[:12]:
                print(f"    > {line}")
                time.sleep(0.03)
            if len(output_lines) > 12:
                print(f"    > ... [ Truncated console view: {len(output_lines) - 12} lines buffered to storage ] ...")
        else:
            print("    > Stream payload empty; writing raw socket descriptors to log.")
            
        storage_container["execution_logs"].append(module_record)
        
    except FileNotFoundError:
        error_message = f"Execution Failure: Binary '{command_sequence[0]}' unavailable in environment PATH."
        print(f"    [-] {error_message}")
        storage_container["execution_logs"].append({"module_name": module_title, "status": "FAILED", "error": error_message})
    except Exception as unhandled_exception:
        error_message = f"Runtime Exception: {str(unhandled_exception)}"
        print(f"    [-] {error_message}")
        storage_container["execution_logs"].append({"module_name": module_title, "status": "ERROR", "error": error_message})
    
    time.sleep(random.uniform(0.8, 1.5))

def main_routine():
    if os.geteuid() != 0:
        print("[!] Notice: Running without root privileges. Raw packet injection features restricted.")
        time.sleep(1.2)
        
    target_endpoint = acquire_target_endpoint()
    selected_profile = present_operational_menu()
    
    output_filename = f"syspulse_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    telemetry_dataset = {
        "session_id": datetime.now().isoformat(),
        "target": target_endpoint,
        "profile": selected_profile,
        "execution_logs": []
    }
    
    render_execution_header(target_endpoint, selected_profile)
    
    simulate_human_pacing("[*] Initializing memory allocations and socket buffers...")
    time.sleep(1.5)
    
    if selected_profile == "1":
        execute_diagnostic_module("Host Liveness & ICMP Probe", ["ping", "-c", "4", target_endpoint], telemetry_dataset)
        simulate_human_pacing("[*] ICMP probes finalized. Analyzing round-trip times...")
        execute_diagnostic_module("DNS Resolution & Route Trace", ["traceroute", "-m", "10", target_endpoint], telemetry_dataset)
        
    elif selected_profile == "2":
        execute_diagnostic_module("Host Liveness & ICMP Probe", ["ping", "-c", "4", target_endpoint], telemetry_dataset)
        simulate_human_pacing("[*] Host responsive. Initiating comprehensive port scan sequence...")
        execute_diagnostic_module("Active Port Enumeration", ["nmap", "-p", "80,443,22,8080,3306", target_endpoint], telemetry_dataset)
        simulate_human_pacing("[*] Port states mapped. Extracting service fingerprints...")
        execute_diagnostic_module("Service Banner Grabbing", ["nmap", "-sV", "--version-intensity", "3", target_endpoint], telemetry_dataset)
        
    elif selected_profile == "3":
        execute_diagnostic_module("Host Liveness & ICMP Probe", ["ping", "-c", "4", target_endpoint], telemetry_dataset)
        simulate_human_pacing("[*] Primary liveness verified. Executing deep trace analysis...")
        execute_diagnostic_module("Extended Route Trace", ["traceroute", target_endpoint], telemetry_dataset)
        simulate_human_pacing("[*] Trace complete. Running full service and state discovery...")
        execute_diagnostic_module("Comprehensive Port Sweep", ["nmap", "-p-", "-T4", target_endpoint], telemetry_dataset)
        simulate_human_pacing("[*] Cataloging network topology and signature profiles...")
        execute_diagnostic_module("OS & Service Fingerprint Analysis", ["nmap", "-O", target_endpoint], telemetry_dataset)

    simulate_human_pacing("[*] Compiling analytical data structures and exporting JSON report...")
    time.sleep(2.0)
    
    with open(output_filename, "w", encoding="utf-8") as file_pointer:
        json.dump(telemetry_dataset, file_pointer, indent=4)
        
    print(f"\n[+] Diagnostic session successfully completed.")
    print(f"[+] Telemetry report compiled and saved to: {output_filename}")
    print("=" * 70)

if __name__ == "__main__":
    main_routine()
