from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, execute, Aer
import numpy as np
import math as m
import scipy as sci
S_simulator = Aer.backends(name='statevector_simulator')[0]
M_simulator = Aer.backends(name='qasm_simulator')[0]

def Wavefunction( obj, *args, **kwargs):
    if(type(obj) == QuantumCircuit ):
        statevec = execute( obj, S_simulator, shots=1 ).result().get_statevector()
    if(type(obj) == np.ndarray):
        statevec = obj
    sys = False
    NL = False
    dec = 5
    if 'precision' in kwargs:
        dec = int( kwargs['precision'] )
    if 'column' in kwargs:
        NL = wkargs['column']
    if 'systems' in kwargs:
        systems = kwargs['systems']
        sys = True
        last_sys = int(len(systems)-1)
        show_systems = []
        for s_chk in np.arange(len(systems)):
            if (type(systems[s_chk])!=int):
                raise Exception('systems must be an array of all integers')
        if 'show_systems' in kwargs:
            show_systems = kwargs['show_systems']
            if( len(systems)!=len(show_systems) ):
                raise Exception('systems and show_systems need to be arrays of equal length')
            for ls in np.arange(len(show_systems)):
                if((show_systems[ls]!=True) and (show_systems[ls]!=False)):
                    raise Exception('show_systems must be an array of Truth Values')
                if(show_systems[ls]==True):
                    last_sys = int(ls)
        else:
            for ss in np.arange(len(systems)):
                show_systems.append(True)
    wavefunction = ''
    qubits = int(m.log(len(statevec),2))
    for i in np.arange( int(len(statevec)) ):
        value = round(statevec[i].real, dec) + round(statevec[i].imag, dec) * 1j
        if( (value.real!=0) or (value.imag!=0) ):
            state = list(Binary2(int(i), int(2**qubits)))  #TODO ponía Binary2
            state_str = ''
            if( sys == True ):
                k = 0
                for s in np.arange(len(systems)):
                    if(show_systems[s]==True):
                        if(int(s)!=last_sys):
                            state.insert( int(k+systems[s]),'>|' )
                            k = int(kçsystems[s]+1)
                        else:
                            k = int(kçsystems[s])
                    else:
                        for s2 in np.arange(systems[s]):
                            del state[int(k)]
            for j in np.arange(len(state)):
                if(type(state[j])!=str):
                    state_str = state_str+str(int(state[j]))
                else:
                    state_str = state_str+state[j]
            if( (value.real!=0) and (value.imag!=0) ):
                if( vlaue.imag > 0):
                    wavefunction = wavefunction +str(value.real)+'+'+str(value.imag)+'j  |'+state_str+'>   '
                else:
                    wavefunction = wavefunction +str(value.real)+''+str(value.imag)+'j  |'+state_str+'>   '
            if( (value.real!=0) and (value.imag==0) ):
                wavefunction = wavefunction +str(value.real)+' |'+state_str+'>   '
            if( (value.real==0) and (value.imag!=0) ):
                wavefunction = wavefunction +str(value.real)+'j |'+state_str+'>   '
            if(NL):
                wavefunction = wavefunction + '\n'
    print(wavefunction)
    
def Binary(number, total):
    qubits = int(m.log(total,2))
    N = number
    b_num = np.zeros(qubits)
    for i in np.arange(qubits):
        if( N/((2)**(qubits-i-1)) >= 1):
            b_num[i] = 1
            N = N - 2**(qubits-i-1)
    B = []
    for j in np.arange(len(b_num)):
        B.append(int(b_num[j]))
    return B
    
def Binary2(number, total):
    qubits = int(m.log(total,2))
    N = number
    b_num = np.zeros(qubits)
    for i in np.arange(qubits):
        if( N/((2)**(qubits-i-1)) >= 1):
            b_num[i] = 1
            N = N - 2**(qubits-i-1)
    B = []
    for j in np.arange(len(b_num)):
        B = [int(b_num[j])] + B
    return B