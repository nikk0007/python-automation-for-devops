#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        file_check_message='',
        failed=False
    )

    module = AnsibleModule(argument_spec=module_args)

    path = module.params['path']

    if os.path.exists(path):
        result['file_check_message'] = f"File {path} exists."
    else:
        result['file_check_message'] = f"File {path} does not exist."
        result['failed'] = True

    module.exit_json(**result)

if __name__ == '__main__':
    run_module()
