#!/usr/bin/python

from ansible.module_utils.basic import *

def run_module():
    #module_args = dict(
    #    name = dict(type='str', required=True),
    #)
    #result['original_message'] = module.params['name']
    #result['message'] = 'goodbye'
    #result['my_useful_info'] = {
    #    'foo': 'bar',
    #    'answer': 42,
    #}
    module = AnsibleModule(argument_spec={})
    theReturnValue = {"mykey": "myvalue"}
    module.exit_json(changed=False, meta=theReturnValue)


def main():
    run_module()

if __name__ == '__main__':
    main()

