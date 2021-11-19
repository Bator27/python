reggeli = {'vaj', 'tea', 'Pirítos'}
reggeli.add('víz')
#reggeli.remove('körte')
reggeli.discard('körte')
print(reggeli)

ebed = {}
#ebed = set['halaszlé', 'kenyér', True ]

print(type( ebed ))
print( ebed )

print( reggeli & ebed )
print( reggeli | ebed )
print( reggeli - ebed )
print( reggeli ^ ebed )

gyumolcskosar = ['eper', 'alma', 'szilvia', 'eper']
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)

