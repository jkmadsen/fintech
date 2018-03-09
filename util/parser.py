def args_to_dict(args):
    ret = {}
    arg_list = args.split(',')
    for arg in arg_list:
        kv = arg.split('=')
        ret[kv[0]] = kv[1]
    return ret
