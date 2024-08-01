"""
Since adapter_config.json contains the base model path of checkpoint
This script is used to automatically modify the checkpoint base model path configuration on the target system after files have been transferred using the SCP protocol.
"""

import os
import json

# all the parameters within this script
root_dir = "checkpoint_path"
# old and new base_model_name_or_path
old_base_model_path = "before_scp_model_path"
new_base_model_path = "after_scp_model_path"


# loop every checkpoint
count=0
for checkpoint_dir in os.listdir(root_dir):
    # if count >0:
    #     break
    checkpoint_path = os.path.join(root_dir, checkpoint_dir)
    adapter_config_path = os.path.join(checkpoint_path, "adapter_config.json")
    
    # check if adapter_config.json exists
    if os.path.exists(adapter_config_path):
        # read JSON 
        with open(adapter_config_path, "r") as file:
            config = json.load(file)
        
        # modify base_model_name_or_path
        if config.get("base_model_name_or_path") == old_base_model_path:
            config["base_model_name_or_path"] = new_base_model_path
            
            # update configure
            with open(adapter_config_path, "w") as file:
                json.dump(config, file, indent=4)
            
            print(f"Updated {adapter_config_path}")
        else:
            print(f"No change needed for {adapter_config_path}")
    else:
        print(f"adapter_config.json not found in {checkpoint_path}")
    # count+=1
