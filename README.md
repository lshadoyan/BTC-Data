# Historical-BTC 
Retrieves historical Bitcoin using the Coinbase API and saves that data into a CSV file called `Bitcoin_data.csv`. 
### Data Retrieved 
 - `Date`, `Open`, `High`, `Low`, `Close` and `volume` with a candle length of 1 hour
## Setup 
### With Docker 
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clone the Repo: 
	````
	git clone https://github.com/lshadoyan/Historical-BTC.git 
	````
3. Navigate to the repo directory and build the Docker image: 
	````
	docker build -t btc_data .
	````
4. Build and run the Docker container:
	````
	docker run -v $(pwd):/app btc_data
	````
	or if on Windows use
	````
	docker run -v %cd%:/app btc_data
	````
	*Alternatively use the absolute path to the repo directory instead of `%cd%` or `$(pwd)` 

### Without Docker
1. Clone the Repo:
	````
	git clone https://github.com/lshadoyan/Historical-BTC.git 
	````
2. Navigate to the repo directory and install the required libraries:
	````
	pip install -r requirements.txt
	````
3. Run the code using:
	````
	python data.py
	```` 
**In both cases, the `.csv` called `Bitcoin_data.csv` should appear in the repo directory**
