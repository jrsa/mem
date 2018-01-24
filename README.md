# mem
convenient wrapper around pyMach using structs. grown out of repl-based exploration and editing of other processes memory. requires pymach and execution as superuser

    from memory import Memory
    import sys
    
     # any process id
    pid = int(sys.argv[1])
    m = Memory(pid)
    
    # read an unsigned integer from any valid address in the foriegn process
    address = 0xDEADBEEF
    value = m.read('I', address)

    # apply hax
    value = value + 1
    
    # write the modified value back
    m.write('I', address, value)
