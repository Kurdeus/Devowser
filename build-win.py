import os
import subprocess
import sys

def run_build_win():
    """
    Executes the build-win.cmd script to build the Windows application.
    Handles script execution, error checking, and provides detailed status output.
    
    Returns:
        bool: True if build succeeded, False if failed
    """
    try:
        # Get script directory and verify build script exists
        script_dir = os.path.dirname(os.path.abspath(__file__))
        build_script = os.path.join(script_dir, "build-win.cmd")
        
        if not os.path.isfile(build_script):
            print(f"❌ Error: Build script not found at {build_script}", file=sys.stderr)
            return False

        print("🚀 Starting Windows build process...")
        
        # Execute build script with real-time output
        process = subprocess.Popen(
            build_script,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        
        # Stream output in real-time
        for line in process.stdout:
            print(line, end='')
            
        # Wait for process to complete and check result
        return_code = process.wait()
        
        if return_code == 0:
            print("✅ Build completed successfully!")
            return True
            
        print(f"❌ Build failed with exit code {return_code}", file=sys.stderr)
        return False
        
    except subprocess.SubprocessError as e:
        print(f"❌ Build process error: {str(e)}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    sys.exit(0 if run_build_win() else 1)
