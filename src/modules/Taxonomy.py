import json

rpr_taxonomy = {
    'remediation': ['repair', 'rpr', 'fix', 'troubleshoot', 'trouble shoot', 'trbl shoot', 'correct', 'modify'],
    'change and replace' : ['replace', 'rplc', 'rpl', 'rep ', 'change', 'chng'],
    'service': ['connect', 'reset', 'restore', 'turn on', 'turn off', 'adjust', 'adj ', 'align', 'seal', 'configure', 'recal', 'calib', 'insulate', 'cap '],
    'manufacture':['weld', 'assemble', 'fabricate', 'manufactur', 'creat', 'make', 'build'],
    'cutting access': ['cut access', 'cutaccess'],
    'separation and deconstruction': ['disassemble', 'dismantle', 'disconnect', 'detach', 'isolate'],
    'cleaning': ['clean', 'discard', 'dispose', 'removal'],
    'moving and delivery': ['box', 'supplies', 'dolly', 'wheel', 'caddy', 'pick up', 'deliver', 'relocate', 'mover', 'moving','driver', 'drop'], #for campus and caretakers
    'assistance':['assist', 'asst', 'help', 'work with'],
    'supply and installation':['install', 'supply', 'provide', 'add', 'upgrade', 'arrange', 'setup', 'set up'],

}

quality_control = {
    'inspection and coordination':['check', 'chk', 'investig', 'coordinate','monitor', 'inspect', 'walk through', 'walkthrough', 'walk thru', 'walkthru', 'escort', 'visit', 'tour'],
    'testing and assessment':['test', 'scan', 'review', 'assess', 'eval', 'inquire', 'locate', 'estimate', 'determine', 'measure', 'verify', 'validate', 'certify', 'recertify'],
    'power and shutdown requests':['power request', 'power shutdown', 'power study', 'power assess', 'power investig', 'shutdown request', 'elec shutdown', 'shutdown'],
    'documentation and reporting':['report', 'audit', 'survey'],
    'scheduled activities':['daily', 'monthly', 'weekly', 'annual', 'routine'],
    }
access_security = {
    'access requests':['access request', 'request access', 'provide access', 'building access', 'room access', 'security access', 'need access'],
    'contractor access': ['contractor access', 'contractor key', 'contractor fob', 'contractor tag'],
    'key services':['rekey', 'make key', 'copy key', 'key copy', 're key', 'key repl', 'provide key', 'need key']}

others = {'follow up': ['follow up'],
          'standing order':['standing order','sor '],
          'mobile status':['mobile status'],
          'billing and time keeping':[' ot ', 'time', 'keep', 'bill', 'overtime', 'over time', 'labour', 'charge'],
          'work order management': ['work manage','order manage']
}

issue_taxonomy = {
    'equipment and component issues':['issue', 'miss', 'trip', 'deficien', 'fail', 'fault', 'blown', 'stick', 'stuck', 'seize', 'malfunction', 'brk', 'break', 'broken', 'brkn', 'crack', 'dead', 'damage', 'loos', 'expos', 'detach', 'hang', 'cave', 'gap', 'plug', 'clog', 'not lock', 'not unlock', 'jam'],
    'operational functionality': ['not start', 'no power', 'not work', 'not respond', 'not flush', 'unresponsive', 'not run', 'not operate', 'not function', 'not shut', 'not close', 'not open', 'not secure', 'not latch', 'not control', 'no control', 'not modulate', 'not switch', 'over press', 'stuck elevator', 'dock plate not secure', 'stuck on loading dock', 'not com', 'not move', 'not travel', 'not go', 'not open', 'poor ride quality'],
    'leakage and spillage': ['leak', 'drip', 'stain', 'wet'],
    'burning and odor': ['burn', 'smoke', 'odor', 'smell'],
    'noise and sound':['noise', 'nois', 'loud', 'squeak', 'buzz', 'hiss', 'rattle', 'strange sound'],
    'water-steam flow issues':['overflow', 'flow over', 'keep run', 'continuous', 'constant', 'no water', 'low pressur', 'high pressur', 'pressure low', 'pressure high', 'pressure too high', 'pressure too low', 'water too hot', 'water too cold', 'no hot water', 'no cold water', 'water temperature', 'low flow', 'low water flow', 'not enough'],
    'wear and corrosion':['corrod', 'rust', 'worn'],
    'safety and hazards':['hazard', 'safety', 'violation', 'unsafe', 'not safe', 'danger', 'concern', 'entrapment'],
    'space comfort issues':['too hot', 'too cold', 'too humid', 'too dry', 'too warm', 'extremely hot', 'extremely cold', 'freezing cold', 'heater not work', 'ac not work', 'ventilation not work', 'fan not work', 'thermostat not work', 'no ventilation', 'poor air'],
    'lighting issues': ['no light', 'spark', 'flicker', 'light out', 'light be out'],
    'alarms':['alarm'],
    'other emergency':['other emergency']}

concept_taxonomy = {
    'toilet and urinal': ['toilet', 'urinal', 'flush'],
    'sink and faucet' :['sink', 'faucet', 'tapwater','tap water'],
    'fountains and eyewash' :['eyewash', 'eye wash', 'fountain', 'water station'],
    'sewage and drainage': [ 'drain','sewage', 'sewer', 'sanitary line','storm line', 'storm pipe',],
    'shower':['shower'],
    'hose and sprinkler':['hose', 'bib', 'sprinkler', 'irrigation'],
    'backflow preventer':['bfp', 'backflow'],
    'water distribution' : ['domestic hot water system', 'dhw', 'domestic water system', 'domestic cold water system', 'dcw'],

    'door, window, hardware': ['door', 'lock', 'key', 'padlock', 'door frame', 'deadbolt', 'maglock', 'window', 'hatch', 'handle', 'shaft', 'latch', 'cylinder', 'closer', 'hinge', 'knob', 'Nob', 'doorknob', 'bolt', 'crossbar', 'lockbox', 'keybox'],
    'fobs and readers': ['fob', 'salto', 'reader', 'detex'],
    'accessibility buttons': ['door button', 'door btn', 'push button', 'accessibility button', 'access button', 'panic button'],

    'electrical systems': ['booster', 'generator', 'breaker', 'switch', 'fuse', 'panel', 'starter', 'vfd', 'inverter', 'junction box', 'css', 'transformer', 'circuit', 'contactor', 'wire', 'wiring', 'conduit', 'tube', 'receptacle', 'outlet', 'generator', 'turbine'],
    'lighting systems': ['light', 'ballast', 'dimmer', 'bulb', 'lamp', 'sign', 'fixture'],

    'valves and controllers': ['prv', 'pressure regulating valve', 'safety valve', 'gate valve', 'ball valve', 'steam valve', 'control valve', 'relief valve', 'rad valve', 'balancing valve', 'heating valve', 'drain valve', 'air valve', 'off valve', 'isolation valve', 'controller', 'compressor', 'condenser', 'cond', 'humidifier', 'motor', 'mtr', 'level controller', 'float level', 'lvl cont', 'air controller', 'jci controller', 'honeywell controller', 'steam controller', 'glycol', 'chw', 'chilled water', 'hwh', 'hot water heating', 'pneumatic'],
    'hvac and ac': ['hvac', 'air circulation', 'air conditioner', 'ac', 'heater', 'ventilation', 'air vent', 'vent', 'airline', 'air line', 'hood', 'fume', 'exhaust', 'exst', 'exh', 'ah', 'air handle', 'ahu', 'thermostat', 'radiator', 'rad', 'fan', 'fancoil', 'coil', 'fcu', 'blade'],
    'fluid handling equipment': ['steam trap', 'gasket', 'chemical dosing', 'dosing line', 'dosing tank', 'pot feeder', 'chemical pot', 'dose pump', 'after filter', 'strainer', 'softener', 'expansion tank', 'flash tank', 'cushion tank', 'brine tank', 'brine', 'autoclave', 'gauge pipe', 'gauge glass', 'flange', 'saddle', 'tee', 'nipple', 'vaccum', 'vaccume breaker', 'vacc', 'tank', 'nitrogen', 'liq'],
    'chillers and boilers': ['chiller', 'boiler'],

    'ceiling and flooring': ['ceil', 'tile', 'flooring'],
    'railing': ['railing', 'rail deck'],
    'scaffolds and supports': ['scaffold', 'wood support', 'bracket'],
    'insulation': ['insulat'],

    'waste and recycling': ['garbage', 'bin', 'recycl', 'waste', 'trash', 'debris'],
    'events and conferences': ['event', 'conf'],
    'film shoot':['shoot','film'], #for caretaker or campus
    'nitrogen cylinders':['nitrogen','liquid'], #only for campus services

    'restroom facilities': ['dispenser', 'towel', 'soap', 'dryer'],
    'furniture': ['furniture', 'board', 'drawer', 'cabinet', 'hook', 'hang', 'tray', 'art', 'chair', 'sofa', 'couch', 'table', 'desk', 'bookcase', 'bookshelf', 'hutch', 'photo', 'deck', 'blind', 'mount', 'chain', 'wedge', 'shelf', 'shelves', 'mat'],
    'computers and equipment': ['tv', 'monitor', 'keyboard', 'computer', 'server', 'printer', 'cartridge', 'toner','laptop','mouse','scanner'],
    'kitchen appliances': ['fridge', 'freezer', 'dishwasher', 'dish washer'],

    'metal sheets and covers': ['checkered plate', 'guard', 'safety rail', 'barricade','filter rack', 'filter frame', 'filt fram', 'fan guard', 'drain cover', 'deflector', 'water shield', 'screen', 'plate', 'sheet metal', 'sheetmetal', 'pan', 'tray', 'metal tile', 'grill', 'diffuser', 'cladding', 'pit cover', 'canopy'],
    'ducts and induction': ['duct', 'duc', 'induction', 'induc', 'flex joint'],
    'machine shop equipment': ['machine shop', 'bracket', 'sheaf', 'sheav', 'bearing', 'nipple', 'mullion', 'bollard', 'pulley', 'mill plate', 'anchor', 'spool', 'stud', 'compactor', 'turbine'],

    'asbestos and abatement':['asbestos','abatement'] #for hcmg
}

dics = [access_security, concept_taxonomy, issue_taxonomy, others, quality_control,
        rpr_taxonomy]
keys = [x for dic in dics for x in dic.keys()]
words = [y for dic in dics for i,j in dic.items() for y in j]

