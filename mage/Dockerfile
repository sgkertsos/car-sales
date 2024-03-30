FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

# Note: this overwrites the requirements.txt file in your new project on first run. 
# You can delete this line for the second run :) 
COPY requirements.txt ${USER_CODE_PATH}/requirements.txt 

# Copy pipelines and blocks
COPY data_exporters/ex_csv_to_gcs.py ${USER_CODE_PATH}/mage-car-prices/data_exporters/ex_csv_to_gcs.py
COPY data_loaders/bl_csv_to_gcs.py ${USER_CODE_PATH}/mage-car-prices/data_loaders/bl_csv_to_gcs.py
COPY pipelines/csv_to_gcs/metadata.yaml ${USER_CODE_PATH}/mage-car-prices/pipelines/csv_to_gcs/metadata.yaml
COPY transformers/tr_fix_dates.py ${USER_CODE_PATH}/mage-car-prices/transformers/tr_fix_dates.py
COPY io_config.yaml ${USER_CODE_PATH}/mage-car-prices/io_config.yaml

RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
