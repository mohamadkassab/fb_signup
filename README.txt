######################################################################  Web automation task by MOHAMAD KASSAB ##################################################################################

Welcome! This README will guide you on how to run the program.
This web automation script is designed to create a predefinied number of accounts on facebook.

	# Prerequisites

		* Download and install python from Python's official website. Make sure to include pip tool
 	 	  and the enviroment variable path from the installation. 

		* Download and install a compatible IDE for python , VSCode is recommended. 

	# Install required libraries

		Open your terminal in vscode and excute the following commands:

		* pip install selenium==4.0 (note: higher version of selenium may not be working, thus it is recommended to use this version)
 
		* pip install requests
	
		* pip install python-dotenv

	# Configurations

		* Go to main.py file and set the variable "number_account_creation" to the number of accounts that you want to create 

		* (optional) In case you want to use your own ip instead of proxies 
 		  you can comment the line number 46 "chrome_options.add_argument(f'--proxy-server={proxy_ip}')"

	# Run the script

		* Open the terminal in vscode and excute the following comman  "python main.py"


######################################################################################## ENJOY ##################################################################################







