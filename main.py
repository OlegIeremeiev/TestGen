import yaml, random, os
from src.question import Question
from src.testdocx import TestDocx


def main(config):
    variants = 20
    students = 20
    tests = generate_test(config, variants)
    write_test(tests, students)


def generate_test(config, variants):
    test = {'general':
                {'discipline': config['discipline'], 'title': config['title'], 'course': config['course'],
                   'filename': config['course'] + "_" + config['name']}
            }
    questions = [[] for x in range(variants)]
    quest_indices = []
    for i in range(len(config['pools'])):
        pool = config['pools'][i]
        size = len(pool['items'])
        if pool['number'] > size:
            print("Error: number don't match to questions count of {0} pool in {1}/{2}.yaml".format(i,config['course'],config['name']))
        elif pool['number'] == size:
            quest_indices = [ [x for x in range(size)] for y in range(variants)]
        elif pool['select'] == 'random':
            quest_indices = [ random.sample(range(0, size), pool['number']) for x in range(variants) ]
        elif pool['select'][0] == '[' and pool['select'][-1] == ']':
            res = [[int(y) for y in x.split(',')] for x in pool['select'][1:-1].split(';')]
            quest_indices = [res[x % len(res)] for x in range(variants)]
        else:
            quest_indices=[ [] for x in range(variants)]
            p_index = 0
            for k in range(pool['number']*variants):
                while p_index in quest_indices[k % variants]:
                    p_index += 1
                    p_index %= size
                quest_indices[k % variants].append(p_index)
                p_index += 1
                p_index %= size

        for row in range(len(quest_indices)):
            for index in quest_indices[row]:
                tmp = pool['items'][index]
                qtmp = Question(tmp)
                if 'app' in tmp:
                    path = 'src'+os.path.sep+'scripts'+os.path.sep+config['course']+os.path.sep+tmp['script']
                    if os.path.isfile(path + '.py'):
                        function_string = path.replace(os.path.sep,'.')+'.'+tmp['script']
                        qtmp.execute(function_string,tmp['parameters'])
                    else:
                        print("Error: script of {0} pool not exists".format(i))
                else:
                    qtmp.shuffle()
                qtmp.index = index
                questions[row].append(qtmp)

    [ random.shuffle(x) for x in questions ]
    test['questions'] = questions
    return test


def write_test(tests, students):
    doc = TestDocx()
    doc.write_test(tests, students)


if __name__ == '__main__':
    configpath = 'tests/cyber/module_2.yaml'
    config = yaml.load(open(configpath,'r'), Loader=yaml.SafeLoader)
    print("{0} : {1}".format(config['course'],config['name']))
    main(config)
