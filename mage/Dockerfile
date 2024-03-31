FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

# Note: this overwrites the requirements.txt file in your new project on first run. 
# You can delete this line for the second run :) 
COPY requirements.txt ${USER_CODE_PATH}/requirements.txt 

# Copy pipelines and blocks
COPY custom/bl_create_partitioned_table.sql ${USER_CODE_PATH}/${PROJECT_NAME}/custom/bl_create_partitioned_table.sql
COPY data_exporters/bl_transfer_data_from_gcs_to_bq.py ${USER_CODE_PATH}/${PROJECT_NAME}/data_exporters/bl_transfer_data_from_gcs_to_bq.py
COPY data_exporters/bl_upload_data_to_gcs.py ${USER_CODE_PATH}/${PROJECT_NAME}/data_exporters/bl_upload_data_to_gcs.py
COPY data_loaders/bl_load_data_from_csv.py ${USER_CODE_PATH}/${PROJECT_NAME}/data_loaders/bl_load_data_from_csv.py
COPY data_loaders/bl_load_data_from_gcs.py ${USER_CODE_PATH}/${PROJECT_NAME}/data_loaders/bl_load_data_from_gcs.py
COPY pipelines/csv_to_gcs/metadata.yaml ${USER_CODE_PATH}/${PROJECT_NAME}/pipelines/csv_to_gcs/metadata.yaml
COPY pipelines/gcs_to_bq/metadata.yaml ${USER_CODE_PATH}/${PROJECT_NAME}/pipelines/gcs_to_bq/metadata.yaml
COPY transformers/bl_transform_data.py ${USER_CODE_PATH}/${PROJECT_NAME}/transformers/bl_transform_data.py
COPY io_config.yaml ${USER_CODE_PATH}/${PROJECT_NAME}/io_config.yaml

RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
