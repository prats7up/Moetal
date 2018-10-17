import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord

coord_frb = [ '(01h18m, -75d12m)', '(18h52m, -08d29m)', '(22h34m, -12d24m)', '(21h03m, -44d44m)', '(23h30m, -02d52m)', '(23h15m, -18d25m)', '(19h07m, -40d37m)', '(18h14m, -85d11m)', '(05h32m, 33d05m)', '(06h44m, -51d17m)', '(22h34m, -12d18m)', '(03h07m, -29d55m)', '(16h27m, -07d27m)', '(09h03m, 03d26m)', '(13h41, -05d59m)', '(21h45m, -00h12m)', '(07h16m, -19d00m)' ]


ra_frb = ['01h18m', '18h52m', '22h34m', '21h03m', '23h30m', '23h15m', '19h07m', '18h14m', '05h32m', '06h44m', '22h34m', '03h07m', '16h27m', '09h03m', '13h41m', '21h45m', '07h16m']
dec_frb = ['-75d12m', '-08d29m', '-12d24m', '-44d44m', '-02d52m', '-18d25m', '-40d37m', '-85d11m', '33d05m', '-51d17m', '-12d18m', '-29d55m', '-07d27m', '03d26m', '-05d59m', '-00d12m', '-19d00m']


solar_ra = ['01h18m', '18h52m', '22h34m', '21h03m', '23h30m', '23h15m', '19h07m', '18h14m', '05h32m', '06h44m', '22h34m', '03h07m', '16h27m', '09h03m', '13h41m', '21h45m', '07h16m']
solar_dec = ['00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m', '00d00m']

#c = SkyCoord( coord_frb, unit=(u.hourangle, u.deg) )
#c = SkyCoord( ('01h18m', '-75d12m'), ('18h52m', '-08d29m') )

c = SkyCoord( ra=ra_frb, dec = dec_frb, unit=(u.hourangle, u.deg) )

gal_coords = c.galactic

c = SkyCoord( ra=solar_ra, dec = solar_dec, unit=(u.hourangle, u.deg) )
c_solar = c.galactic 



fig = plt.figure()
ax = fig.add_subplot(111, projection="mollweide")
# -pi<l<pi; -pi/2<b<pi/2
#ax.scatter(gal_coords.l.wrap_at(180*u.degree).radian, gal_coords.b.radian)
#ax.scatter(c_solar.l.wrap_at(180*u.degree).radian, c_solar.b.radian)

c = SkyCoord.from_name("M 82", frame='icrs')
ax.scatter(c.ra.wrap_at(180*u.degree).radian, c.dec.radian)
c = SkyCoord.from_name("NGC 253", frame='icrs')
ax.scatter(c.ra.wrap_at(180*u.degree).radian, c.dec.radian)
plt.show()
