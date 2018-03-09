def args_to_dict(args):
    ret = {}
    try:
        arg_list = args.split(',')
        for arg in arg_list:
            if arg != '' and arg != None and arg != 'None':
                kv = arg.split('=')
                ret[kv[0]] = kv[1]
    except:
        print 'Could not parse additional arguments'
    return ret
