#!/usr/bin/env python
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor


#inventory = Inventory(loader=loader, variable_manager=variable_manager,host_list='/home/felixc/ansible/hosts')
loader = DataLoader()
inventory = InventoryManager(loader=loader, sources=['./hostslist'])
variable_manager = VariableManager(loader=loader, inventory=inventory)

passwords=dict(vault_pass='0koooAdmin')

Options = namedtuple('Options',
                     ['connection',
                      'remote_user',
                      'ask_sudo_pass',
                      'verbosity',
                      'ack_pass', 
                      'module_path', 
                      'forks', 
                      'become', 
                      'become_method', 
                      'become_user', 
                      'check',
                      'listhosts', 
                      'listtasks', 
                      'listtags',
                      'syntax',
                      'sudo_user',
                      'sudo',
                      'diff'])

options = Options(connection='smart', 
                       remote_user=None,
                       ack_pass=None,
                       sudo_user=None,
                       forks=5,
                       sudo=None,
                       ask_sudo_pass=False,
                       verbosity=5,
                       module_path=None,  
                       become=None, 
                       become_method=None, 
                       become_user=None, 
                       check=False,
                       diff=False,
                       listhosts=None,
                       listtasks=None, 
                       listtags=None, 
                       syntax=None)


playbook = PlaybookExecutor(playbooks=['ansi_conf/198.yml'],inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,options=options,passwords=passwords)
playbook.run()