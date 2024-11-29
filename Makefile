
# Variables
PYTHON := python3
SCRIPTS := \
    conductP1.py \
    conductP2.py \
    conductP3.py \

    # If you do not need to request optimized prompts, comment out there lines
    # refineTask.py \
    # refineContext.py \
    # refineRemove.py \

    conductP1E.py \
    conductP2E.py \
    conductP3E.py \

    # If you do not need to request optimized prompts, comment out there lines
    # refineCheck.py \
    # refineExtend.py \
    # refineFine.py \

    requestTask.py \
    requestContext.py \
    requestRemove.py \
    requestCheck.py \
    requestExtend.py \
    requestFine.py


all: run_scripts


run_scripts:
	@echo "Starting execution of scripts..."
	@for script in $(SCRIPTS); do \
		echo "Running $$script..."; \
		$(PYTHON) $$script || { echo "Error executing $$script"; exit 1; }; \
	done
	@echo "All scripts executed successfully."

# Clean up (optional, if needed for temporary files)
clean:
	@echo "Cleaning up temporary files..."
	@rm -f *.tmp
	@echo "Clean up completed."
