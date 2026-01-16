import math
import time
from rich.table import Table
from rich.console import Console
import click
import sys

email='markmacgh@gmail.com/hecateare@gmail.com' 

class Astro:
    '''an astrophysics engine'''
    def __init__(self,tble=None):
        self.k_1='a planet orbits the sun in an ellipse with the sun at one focus of the ellipse'
        self.k_2='a planet moves faster at perihelion and slowest at aphelion..A line connecting a planet to the sun sweeps out equal areas in equal time intervals'
        self.k_3='the square of the orbital period of a planet is proportional to the cube of its semi major axis (P**2==a**3)'
        self.AU_m=1.496e11
        self.earthperiod_d=365.25
        self.c_m_s=2.998e8
        self.c_km_s=2.998e5
        self.m='smaller mass'
        self.MoS_kg=1.989e30
        self.MoE_kg=5.972e24
        self.radiusof_Earth_m=6.371e6
        self.earthperiod_s=3.156e7
        self.earthorbit_velocity_km_s=29.78
        self.eccentricity='c/a (where c is the distance from the center of the ellipse to its focus). or using the apsides r_a-r_p/r_a+r_p'

        #...SOLAR SYSTEM_mass in terms of Earth...

        self.Mercury_mass=0.05528
        self.Venus_mass=0.81500
        self.Earth_mass=1.0000
        self.Mars_mass=0.10745
        self.Ceres_mass=0.00016
        self.Jupiter_mass=317.83
        self.Saturn_mass=95.159
        self.Uranus_mass=14.536
        self.Neptune_mass=17.147
        self.Pluto_mass=0.0021
        self.Eris_mass=0.002

        #...SOLAR SYSTEM_Equitorial Radius in terms of Earth...

        self.Mercury_R=0.3825
        self.Venus_R=0.9488
        self.Earth_R=1.0000
        self.Mars_R=0.5326
        self.Ceres_R=0.076
        self.Jupiter_R=11.209
        self.Saturn_R=9.4492
        self.Uranus_R=4.0073
        self.Neptune_R=3.8826
        self.Pluto_R=0.178
        self.Eris_R=0.188

        #...SOLAR SYSTEM_AU in terms of Earth...

        self.Mercury_AU=0.3871
        self.Venus_AU=0.7233
        self.Earth_AU=1.0000
        self.Mars_AU=1.5236
        self.Ceres_AU=2.767
        self.Jupiter_AU=5.2044
        self.Saturn_AU=9.5826
        self.Uranus_AU=19.2012
        self.Neptune_AU=30.0476
        self.Pluto_AU=39.4817
        self.Eris_AU=67.89

        #...SOLAR SYSTEM_P (year) in terms of Earth...

        self.Mercury_P=0.2408
        self.Venus_P=0.6152
        self.Earth_P=1.0000
        self.Mars_P=1.8808
        self.Ceres_P=4.603
        self.Jupiter_P=11.8618
        self.Saturn_P=29.4567
        self.Uranus_P=84.0107
        self.Neptune_P=164.79
        self.Pluto_P=247.68
        self.Eris_P=559
        
        #...SOLAR SYSTEM_rP (perihelion) in terms of  earths AU..
        
        self.Mercury_rP=0.307
        self.Venus_rP=0.718
        self.Earth_rP=0.983
        self.Mars_rP=1.382
        self.Ceres_rP=2.558
        self.Jupiter_rP=4.950
        self.Saturn_rP=9.048
        self.Uranus_rP=18.286
        self.Neptune_rP=29.810
        self.Pluto_rP=29.660
        self.Haumea_rP=35.150
        self.Makemake_rP=38.520
        self.Eris_rP=37.800

        #...SOLAR SYSTEM_rA (aphelion) AU...

        self.Mercury_rA=0.467
        self.Venus_rA=0.728
        self.Earth_rA=1.017
        self.Mars_rA=1.666
        self.Ceres_rA=2.984
        self.Jupiter_rA=5.458
        self.Saturn_rA=10.057
        self.Uranus_rA=20.110
        self.Neptune_rA=30.330
        self.Pluto_rA=49.300
        self.Haumea_rA=51.540
        self.Makemake_rA=53.050
        self.Eris_rA=97.650

        #...SOLAR SYSTEM_AU...

        self.Mercury_AU=0.387
        self.Venus_AU=0.723
        self.Earth_AU=1.000
        self.Mars_AU=1.524
        self.Ceres_AU=2.771
        self.Jupiter_AU=5.204
        self.Saturn_AU=9.555
        self.Uranus_AU=19.198
        self.Neptune_AU=30.070
        self.Pluto_AU=39.480
        self.Haumea_AU=43.340
        self.Makemake_AU=45.780
        self.Eris_AU=67.730

        #...SOLAR SYSTEM_e...

        self.Mercury_e=0.206
        self.Venus_e=0.007
        self.Earth_e=0.017
        self.Mars_e=0.093
        self.Ceres_e=0.080
        self.Jupiter_e=0.048
        self.Saturn_e=0.056
        self.Uranus_e=0.046
        self.Neptune_e=0.010
        self.Pluto_e=0.250
        self.Haumea_e=0.190
        self.Makemake_e=0.160
        self.Eris_e=0.440

        self.G_2=3.3365e-11 # self.G/2
        self.light_year_m=self.c_m_s*self.earthperiod_s
        self.parsec_m=3.0857e16
        self.parsec_AU=2.0626e5
        self.M='larger Mass'
        self.v='velocity'
        self.newton_3='the magnitude of the force exerted on (M) by (m) must be equal the magnitude of the force exerted on m by M'
        self.orbital_period_2='orbital_period=(2*math.pi*distance)/velocity'
        self.G=6.673e-11
        self.circular='for a CIRCULAR orbit the gravitational force provides the centripetal force'
        self.centripetal_force='centripetal_force=(mass*(velocity**2))/distance'
        self.centripetal_2='G=(self.G*Mass*mass)/(distance**2)'
        self.orbital_velocity_of_planet='orbital_velocity_of_planet=(2*math.pi*distance)/orbital_period'
        self.orbital_velocity='orbital_velocity_of_object=math.sqrt((self.G*mass)/distance)'
        self.orbital_period='orbitalearth_period_2=math.sqrt(4*(math.pow(math.pi,2)*math.pow(self.AU_m,3))/(self.G*self.MoS_kg))'

        self.help='\nlisting of function arguments respectively:\n(harmonic fxn): 1.velocity||2.distance btwn the two objects/masses||3.mass||4.Mass||5. o_p -period in seconds-\n(eccent fxn): 1.r_a -aphelion-||2.r_p -perihelion-||3.tble -triggers a table if not None-\n(energy fxn): 1.k_e -kinetic energy magnitude-||2.p_e -potential energy magnitude-||3.mass -mass of smaller mass-||4.Mass -mass of larger Mass-||5.distance -distance r-\n...use seconds, meters...'                                                                                      

        if tble:
            table=Table(title='...SOLAR SYSTEM...')
            console=Console()                                                  
            table.add_column('Planet/dwarf',style='Cyan')
            table.add_column('(M)ass_kg',style='magenta')
            table.add_column('Equitorial\nRadius\n(R)',style='Cyan')
            table.add_column('Semimajor\nAxis\n(AU)',style='magenta')
            table.add_column('Sidereal\nOrbital\nperiod\n(yr)',style='Cyan')
            table.add_row('Mercury',f'{self.Mercury_mass}',f'{self.Mercury_R}',f'{self.Mercury_AU}',f'{self.Mercury_P}')
            table.add_row('Venus',f'{self.Venus_mass}',f'{self.Venus_R}',f'{self.Venus_AU}',f'{self.Venus_P}')
            table.add_row('Earth',f'{self.Earth_mass}',f'{self.Earth_R}',f'{self.Earth_AU}',f'{self.Earth_P}')
            table.add_row('Mars',f'{self.Mars_mass}',f'{self.Mars_R}',f'{self.Mars_AU}',f'{self.Mars_P}')
            table.add_row('Ceres',f'{self.Ceres_mass}',f'{self.Ceres_R}',f'{self.Ceres_AU}',f'{self.Ceres_P}')
            table.add_row('Jupiter',f'{self.Jupiter_mass}',f'{self.Jupiter_R}',f'{self.Jupiter_AU}',f'{self.Jupiter_P}')
            table.add_row('Saturn',f'{self.Saturn_mass}',f'{self.Saturn_R}',f'{self.Saturn_AU}',f'{self.Saturn_P}')
            table.add_row('Uranus',f'{self.Uranus_mass}',f'{self.Uranus_R}',f'{self.Uranus_AU}',f'{self.Uranus_P}')
            table.add_row('Neptune',f'{self.Neptune_mass}',f'{self.Neptune_R}',f'{self.Neptune_AU}',f'{self.Neptune_P}')
            table.add_row('Pluto',f'{self.Pluto_mass}',f'{self.Pluto_R}',f'{self.Pluto_AU}',f'{self.Pluto_P}')
            table.add_row('Eris',f'{self.Eris_mass}',f'{self.Eris_R}',f'{self.Eris_AU}',f'{self.Eris_P}')
            console.print(table)

            print()
            console.print(f'[bold green]..(m)ass of Earth: {self.MoE_kg}\n..Average distance of Earth from sun: {self.AU_m}\n..Sidereal period of Earth in seconds: {self.earthperiod_s}\n..Equitorial Radius of Earth: {self.radiusof_Earth_m}[/bold green]')
            sys.exit(0)



    def harmonic(self,velocity: float=1,distance: float=1,mass: float=1,Mass: float=1,o_p: float=1):
        start=time.perf_counter()
        '''the harmonic law and how it translates to the universal gravitation constant (mass=smaller-mass) (Mass=larger-mass)'''
        console=Console()
        harmonic_law='P**2==a**3 (or) P**2==kr**3'
    # where k is a constant of proportionality
        orbitalearth_period=(2*math.pi*self.AU_m)/(self.earthorbit_velocity_km_s*1000)
        orbital_velocity_of_earth=(2*math.pi*self.AU_m)/orbitalearth_period
        orbitalearth_period_2=math.sqrt(4*(math.pow(math.pi,2)*math.pow(self.AU_m,3))/(self.G*self.MoS_kg))
        centripetal_force=(mass*(velocity**2))/distance
        orbital_velocity_of_object=math.sqrt((self.G*Mass)/distance) # can also be used to calculate the orbital velocity of planet with circular orbit.

        escape_velocity=math.sqrt((2*(self.G*Mass))/distance)

    #for other planets..
        orbitalperiod_other=math.sqrt(4*(math.pow(math.pi,2)*math.pow(distance,3))/(self.G*self.MoS_kg))
        orbital_velocityother=(2*math.pi*distance)/o_p
        
        #print(f'(Newton-s third law of motion: {instance.newton_3})\n(Kepler-s third law for planets orbits: {instance.k_3})\n(The harmonic law states that {harmonic_law})\nusing ({instance.orbital_period}) and ({instance.centripetal_force})...now substituteusing the second value for the harmonic_law\n({instance.circular}) therefore ({instance.centripetal_2}) which is the gravitational force=the centripetal_force ({instance.centripetal_force}) after solving the resulting equation and putting it in terms of the constant velocity of ({instance.m}), we get the equation for the orbital velocity of an object in circular orbit about ({instance.m}) like earth and a satellite: ({instance.orbital_velocity})\n')
        
        console.print(f'[bold green]...Total time taken by the program: {round(time.perf_counter()-start,2)} (seconds)...[/bold green]')
        print(f'\nCentripetal_Force_btwn_two objects={centripetal_force} (N)\norbitalearth_period={orbitalearth_period} (seconds) # Earths orbital period\norbital_velocity_of_earth={orbital_velocity_of_earth} (m/s) or {orbital_velocity_of_earth/1000} (km/s) # Earths orbital velocity\norbital_velocity_of_object={orbital_velocity_of_object} (m/s)\norbitalearth_period_2={orbitalearth_period_2} (seconds) # Earths orbital period_2\nescape_velocity={escape_velocity} (m/s)\norbitalperiod_other={orbitalperiod_other} (seconds) # Orbital period of other mass\norbital_velocityother = {orbital_velocityother} (m/s) or {orbital_velocityother/1000} (km/s) # Orbital velocity of other mass\n')


    def tebl(self):
        table=Table(title='...ENERGY ECCENT...')
        console=Console()

        table.add_column('Orbit',style='Cyan')
        table.add_column('Eccentricity',style='magenta')
        table.add_column('Total-energy- (E)',style='Cyan')
        table.add_column('Example',style='magenta')
        table.add_row('Circular','e=0','E<0-(mostly negative)-','ISS,Satellites')
        table.add_row('Elliptical','0<e<1','E<0','planets,moons')
        table.add_row('Parabolic','e=1','E=0','Escape Trajectory')
        table.add_row('Hyperbolic','e>1','E>0','Interstellar Objects')
        console.print(table)


    def distance(self,parallax: float=1,distance: float=1,light_years: float=1):
        '''using trigonometric parallax because a nearby star exhibits an annual back and forth change in its position against the stationary background *much more distant stars*'''
        distance_p = 1/parallax # distance_d is in parsec parallax-second
        distance_AU = distance_p*self.parsec_AU
        #distance_AU_m = distance_AU*self.AU_m
        distance_m = distance_p*self.parsec_m
        distance_ly = round((distance_m/self.light_year_m),3)

        #if distance!=1: # variable distance_ps, parallax_t, light year will only be created if the statement is True
        distance_ps = distance/self.parsec_m
        distance_AU_2 = distance_ps*self.parsec_AU
        light_year = round((distance/self.light_year_m),3)
        parallax_t = 1/distance_ps
        
        #if light_years!=1: # the following variables will only be created if the statement is True
        distance_m_2 = light_years*self.light_year_m
        distance_ps_2 = distance_m_2/self.parsec_m
        distance_AU_3 = distance_ps_2*self.parsec_AU
        parallax_t_2 = 1/distance_ps_2


        print(f'\ndistance in parsecs: {distance_p if distance_p!=1 else distance_ps if distance_ps!=3.2407557442395566e-17 else distance_ps_2} (parsecs)\ndistance in AU: {distance_AU if distance_AU!=self.parsec_AU else distance_AU_2 if distance_AU_2!=6.68438279806851e-12 else distance_AU_3} (AU)\nNumber of light years: {distance_ly if distance_ly!=3.261 else light_year if light_year!=0 else light_years} (light years)\ndistance in meters: {distance_m if distance_m!=self.parsec_m else distance_m_2 if distance_m_2!=1.0568938650270438e-16 else distance} (m)\nparallax angle value: {parallax_t if parallax_t!=3.0857e+16 else parallax_t_2 if parallax_t_2!=3.2612573993139486 else parallax}')
        

        



    def timee(self,Mass: float=1,distance: float=1,coordinate_time: float=1,proper_time: float=1):
        '''time dilation due to gravitational fields'''

        # Time passes slower in stronger gravitational fields. Time passes slower for an object moving at high speeds relative to an stationary observer.
        console=Console()
        #pr = (2*self.G*Mass/(distance*math.pow(self.c_m_s,2)))
        #print(pr)
        #exit()
        #proper = math.sqrt(1-pr)

        proper = math.sqrt(abs(1-(2*self.G*Mass/(distance*math.pow(self.c_m_s,2)))))*coordinate_time # shows the fraction of coordinate time that passes as proper time. if one second or hour has passed for the distant stationary observer then the result of the equation is the fraction of coordinate time that has passed as proper time near the mass M.
        #coordinate = 1/(math.sqrt(abs(1-(2*self.G*Mass/(distance*math.pow(self.c_m_s,2))))))*proper_time #Time dilation factor. shows how much more coordinate time passes compared to proper time
        coordinate = 1/(math.sqrt(abs(1-(2*self.G*Mass/(distance*math.pow(self.c_m_s,2))))))*proper_time 

        print(f'\nproper_time: {proper}\ncoordinate_time: {coordinate}\nexplanation: {console.print(f"[bold yellow]for every one unit of time that is measured for a distant stationary object only {proper} has passed for the object at or near the Masses surface and for every one unit of time that is measured for an object near the mass only {coordinate} has passed for the distant stationary object[/bold yellow]")}')


    def energy(self,k_e: float=1,p_e: float=1,mass: float=1,Mass: float=1,distance: float=1,tble=None):
        '''calculates the total mechanical energy of an orbiting body'''
        console=Console()
        kinetic_energy = ((self.G*Mass*mass)/(2*distance)) #k=-E, k=-1/2U where U is the potential energy. E=-k
        potential_energy = -((self.G*Mass*mass)/distance)
        total_energy = -((self.G*Mass*mass)/(2*distance)) #E=1/2U where U is the potential energy.
        # kinetic energy is the negative of the total energy
        total_energy_2 = kinetic_energy+potential_energy if kinetic_energy!=self.G_2 and potential_energy!=-self.G else k_e+p_e

        if total_energy==-self.G_2 and total_energy_2<0:
            console.print('\n[bold yellow]bound orbit..ellipse or circle[/bold yellow]\n') #when k_e, p_e are used to calculate the total_energy
        elif total_energy!=-self.G_2 and total_energy<0 and total_energy_2<0: #total_energy!=-self.G and total_energy_2==2:,,when massee and r are used to calculate E
            console.print('\n[bold yellow]bound orbit..ellipse or circle[/bold yellow]\n')
        elif total_energy==0 or total_energy_2==0:
            console.print('\n[bold yellow]Parabolic orbit.[/bold yellow]\n')
        elif total_energy>0 or total_energy_2>0:
            console.print('\n[bold yellow]unbound orbit..hyperbolic orbit[/bold yellow]\n')

        print(f'\nkinetic_energy: {round(kinetic_energy if kinetic_energy!=self.G_2 else k_e,3)} (Joules or kg.m^2.s^-2)\npotential_energy: {round(potential_energy if potential_energy!=-self.G else p_e,3)} (Joules or kg.m^2.s^-2)\ntotal_energy: {round(total_energy if total_energy!=-self.G_2 else total_energy_2,3)} (Joules or kg.m^2.s^-2)\n')


    def orbit(self,days_elapsed: int=0,period: int=-1,planet: int=None,eccentric=None): # default for planet is Earth
        '''using days, it calculates the position of a planet in a perfect circle. just an example. Planet orbits are eccentric'''
        console=Console()
        mean_motion=None
        mean_anomaly=None
        x_coord=None
        y_coord=None
        if planet:
            if 1<=planet<=11:
                print('initializing...')
            else:
                print('\nonly supports 11 objects in the solar system.check the table contained in the initializing function to see the objects.use 1--11.\n')
                sys.exit(0)

                # or use .get() to get the values if pkanet==1 ..pmanet==11 and a fallback value = period if period!=-1

        values={'1':88,'2':225,'3':365,'4':687,'5':1681,'6':4333,'7':10759,'8':30685,'9':60190,'10':90465,'11':204174} # the values are the period in days. used 365.25
        vallues={'1':self.Mercury_e,'2':self.Venus_e,'3':self.Earth_e,'4':self.Mars_e,'5':self.Ceres_e,'6':self.Jupiter_e,'7':self.Saturn_e,'8':self.Uranus_e,'9':self.Neptune_e,'10':self.Pluto_e,'11':self.Eris_e}
        valllues={'88':self.Mercury_e,'225':self.Venus_e,'365':self.Earth_e,'687':self.Mars_e,'1681':self.Ceres_e,'4333':self.Jupiter_e,'10759':self.Saturn_e,'30685':self.Uranus_e,'60190':self.Neptune_e,'90465':self.Pluto_e,'204174':self.Eris_e} #i can only use the vallues dictionary
        val={'1':self.Mercury_AU,'2':self.Venus_AU,'3':self.Earth_AU,'4':self.Mars_AU,'5':self.Ceres_AU,'6':self.Jupiter_AU,'7':self.Saturn_AU,'8':self.Uranus_AU,'9':self.Neptune_AU,'10':self.Pluto_AU,'11':self.Eris_AU}


        if days_elapsed!=0 and eccentric==None:
            mean_motion=360/(values['1'] if planet==1 else values['2'] if planet==2 else values['3'] if planet==3 else values['4'] if planet==4 else values['5'] if planet==5 else values['6'] if planet==6 else values['7'] if planet==7 else values['8'] if planet==8 else values['9'] if planet==9 else values['10'] if planet==10 else values['11'] if planet==11 else values['3'])  #else earths period 365. nafaa ku update ya period.
            #print(mean_motion,'mean motion for circular orbit')

            mean_anomaly=mean_motion*days_elapsed
            x_coord=math.cos(math.radians(mean_anomaly))
            y_coord=math.sin(math.radians(mean_anomaly))
            
            console.print(f'[bold yellow]For day {days_elapsed}: {(x_coord,y_coord)}')

            #del mean_motion
            #del mean_anomaly               
            #del x_coord
            #del y_coord

        if period!=-1 and eccentric==None:
            table=Table(title='...SOLAR SYSTEM FOR CIRCULAR ORBIT...')
            table.add_column('Day',style='Cyan')
            table.add_column('Angle\n(degrees)',style='magenta')
            table.add_column('Radians',style='Cyan')
            table.add_column('x-Coord',style='magenta')
            table.add_column('y-Coord',style='Cyan') # all of this should be in the if statement..next

        #if period!=-1:
            for day in range(period+1):
                mean_motion=360/period #period in days
                mean_anomaly=mean_motion*day
                radian=math.radians(mean_anomaly)
                x_coord=math.cos(math.radians(mean_anomaly))
                y_coord=math.sin(math.radians(mean_anomaly))
                #console.print(f'\n[bold yellow]Day {day}: {(x_coord,y_coord)}[/bold yellow]\n')
                table.add_row(f'{day}',f'{mean_anomaly}',f'{radian}',f'{x_coord}',f'{y_coord}')
            
            console.print(table)

            #del mean_motion
            #del mean_anomaly
            #del x_coord
            #del y_coord
            

        if eccentric:
            if days_elapsed!=0:
                mean_motion = days_elapsed/(values['1'] if planet==1 else values['2'] if planet==2 else values['3'] if planet==3 else values['4'] if planet==4 else values['5'] if planet==5 else values['6'] if planet==6 else values['7'] if planet==7 else values['8'] if planet==8 else values['9'] if planet==9 else values['10'] if planet==10 else values['11'] if planet==11 else period if period!=-1 else values['3'])
# add a vonsole.print for days_elapsed..
                #print(mean_motion,'mean_motion for elleptic orbit')

                mean_anomaly=mean_motion*(2*math.pi) #2*pi=360 degrees. true anomaly==M..converted into radians
                eccentric_anomaly=mean_anomaly #start with a guess eg E=M
                print('mean anomaly for elliptic orbit:',mean_anomaly)
                #print(eccentric_anomaly,'eccentric anomaly')
                    # using the Newton raphson method
                for i in range(5): 
                    eccentric_anomaly = eccentric_anomaly-((eccentric_anomaly-(vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e)*math.sin(eccentric_anomaly)-mean_anomaly)/(1-((vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e)*math.cos(eccentric_anomaly))))
                    
                print('eccentric anomaly after the newton raphson loop:',eccentric_anomaly)
                

                #use self. instead of the countless dictionaries

                #position=((val['1'] if planet==1 else val['2'] if planet==2 else val['3'] if planet==3 else val['4'] if planet==4 else val['5'] if planet==5 else val['6'] if planet==6 else val['7'] if planet==7 else val['8'] if planet==8 else val['9'] if planet==9 else val['10'] if planet==10 else val['11'] if planet==11 else val['1'] if period==88 else val['2'] if period==225 else val['3'] if period==365 else val['4'] if period==687 else val['5'] if period==1681 else val['6'] if period==4333 else val['7'] if period==10759 else val['8'] if period==30685 else val['9'] if period==60190 else val['10'] if period==90465 else val['11'] if period==204174 else self.Earth_AU)*(1-(self.Mercury_e if planet==1 else self.Venus_e if planet==2 else self.Earth_e if planet==3 else self.Mars_e if planet==4 else self.Ceres_e if planet==5 else self.Jupiter_e if planet==6 else self.Saturn_e if planet==7 else self.Uranus_e if planet==8 else self.Neptune_e if planet==9 else self.Pluto_e if planet==10 else self.Eris_e if planet==11 else self.Mercury_e if period==88 else self.Venus_e if period==225 else self.Earth_e if planet==365 else self.Mars_e if period==687 else self.Ceres_e if period==1681 else self.Jupiter_e if period==4333 else self.Saturn_e if period==10759 else self.Uranus_e if period==30685 else self.Neptune_e if period==60190 else self.Pluto_e if period==90465 else self.Eris_e if period==204174)*math.cos(eccentric_anomaly)))
                b = (self.Mercury_AU if planet==1 else self.Venus_AU if planet==2 else self.Earth_AU if planet==3 else self.Mars_AU if planet==4 else self.Ceres_AU if planet==5 else self.Jupiter_AU if planet==6 else self.Saturn_AU if planet==7 else self.Uranus_AU if planet==8 else self.Neptune_AU if planet==9 else self.Pluto_AU if planet==10 else self.Eris_AU if planet==11 else self.Mercury_AU if period==88 else self.Venus_AU if period==225 else self.Earth_AU if period==365 else self.Mars_AU if period==687 else self.Ceres_AU if period==1681 else self.Jupiter if period==4333 else self.Saturn_AU if period==10759 else self.Uranus_AU if period==30685 else self.Neptune_AU if period==60190 else self.Pluto_AU if period==90465 else self.Eris_AU if period==204174 else self.Earth_AU)*math.sqrt(1-math.pow(vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e,2))
                

                x_coord=(self.Mercury_AU if planet==1 else self.Venus_AU if planet==2 else self.Earth_AU if planet==3 else self.Mars_AU if planet==4 else self.Ceres_AU if planet==5 else self.Jupiter_AU if planet==6 else self.Saturn_AU if planet==7 else self.Uranus_AU if planet==8 else self.Neptune_AU if planet==9 else self.Pluto_AU if planet==10 else self.Eris_AU if planet==11 else self.Mercury_AU if period==88 else self.Venus_AU if period==225 else self.Earth_AU if period==365 else self.Mars_AU if period==687 else self.Ceres_AU if period==1681 else self.Jupiter_AU if period==4333 else self.Saturn_AU if period==10759 else self.Uranus_AU if period==30685 else self.Neptune_AU if period==60190 else self.Pluto_AU if period==90465 else self.Eris_AU if period==204174 else self.Earth_AU)*(math.cos(eccentric_anomaly)-(vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e))
                    
                y_coord=(b*math.sin(eccentric_anomaly))
                console.print(f'\n[bold yellow]Day {days_elapsed}: ({x_coord},{y_coord})[/bold yellow]\n')
            
            if period!=-1 and days_elapsed==0:
                lis_t = [88,225,365,687,1681,4333,10759,30685,60190,90465,204174]

                if period not in lis_t: #enforcer
                    console.print('\n[bold magenta] invalid period![/bold magenta]\n')
                    sys.exit(0)


                table=Table(title='...SOLAR SYSTEM FOR eccentric orbit...')
                table.add_column('Day',style='Cyan')
                table.add_column('Radian',style='magenta')
                table.add_column('eccentric anomaly',style='Cyan')
                table.add_column('x_coord',style='magenta')
                table.add_column('y_coord',style='Cyan')



                for day in range(period+1):

                    mean_motion = day/(values['1'] if planet==1 else values['2'] if planet==2 else values['3'] if planet==3 else values['4'] if planet==4 else values['5'] if planet==5 else values['6'] if planet==6 else values['7'] if planet==7 else values['8'] if planet==8 else values['9'] if planet==9 else values['10'] if planet==10 else values['11'] if planet==11 else period if period!=-1 else values['3'])

                    mean_anomaly=mean_motion*(2*math.pi)
                    eccentric_anomaly=mean_anomaly



                    for i in range(5):
                        eccentric_anomaly = eccentric_anomaly-((eccentric_anomaly-(vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e)*math.sin(eccentric_anomaly)-mean_anomaly)/(1-((vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e)*math.cos(eccentric_anomaly))))


                    b = (self.Mercury_AU if planet==1 else self.Venus_AU if planet==2 else self.Earth_AU if planet==3 else self.Mars_AU if planet==4 else self.Ceres_AU if planet==5 else self.Jupiter_AU if planet==6 else self.Saturn_AU if planet==7 else self.Uranus_AU if planet==8 else self.Neptune_AU if planet==9 else self.Pluto_AU if planet==10 else self.Eris_AU if planet==11 else self.Mercury_AU if period==88 else self.Venus_AU if period==225 else self.Earth_AU if period==365 else self.Mars_AU if period==687 else self.Ceres_AU if period==1681 else self.Jupiter if period==4333 else self.Saturn_AU if period==10759 else self.Uranus_AU if period==30685 else self.Neptune_AU if period==60190 else self.Pluto_AU if period==90465 else self.Eris_AU if period==204174 else self.Earth_AU)*math.sqrt(1-math.pow(vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e,2))
                    
                    x_coord=(self.Mercury_AU if planet==1 else self.Venus_AU if planet==2 else self.Earth_AU if planet==3 else self.Mars_AU if planet==4 else self.Ceres_AU if planet==5 else self.Jupiter_AU if planet==6 else self.Saturn_AU if planet==7 else self.Uranus_AU if planet==8 else self.Neptune_AU if planet==9 else self.Pluto_AU if planet==10 else self.Eris_AU if planet==11 else self.Mercury_AU if period==88 else self.Venus_AU if period==225 else self.Earth_AU if period==365 else self.Mars_AU if period==687 else self.Ceres_AU if period==1681 else self.Jupiter_AU if period==4333 else self.Saturn_AU if period==10759 else self.Uranus_AU if period==30685 else self.Neptune_AU if period==60190 else self.Pluto_AU if period==90465 else self.Eris_AU if period==204174 else self.Earth_AU)*(math.cos(eccentric_anomaly)-(vallues['1'] if planet==1 else vallues['2'] if planet==2 else vallues['3'] if planet==3 else vallues['4'] if planet==4 else vallues['5'] if planet==5 else vallues['6'] if planet==6 else vallues['7'] if planet==7 else vallues['8'] if planet==8 else vallues['9'] if planet==9 else vallues['10'] if planet==10 else vallues['11'] if planet==11 else valllues['88'] if period==88 else valllues['225'] if period==225 else valllues['365'] if period==365 else valllues['687'] if period==687 else valllues['1681'] if period==1681 else valllues['4333'] if period==4333 else valllues['10759'] if period==10759 else valllues['30685'] if period==30685 else valllues['60190'] if period==60190 else valllues['90465'] if period==90465 else valllues['204174'] if period==204174 else self.Earth_e))

                    y_coord=(b*math.sin(eccentric_anomaly))

                    table.add_row(f'{day}',f'{mean_anomaly}',f'{eccentric_anomaly}',f'{x_coord}',f'{y_coord}')

                console.print(table)



                        




    def eccent(self,r_a: float=1,r_p: float=1,tble=None):
        ''' eccentricity is a measure of how much an orbit deviates from being a perfect circle'''
        console=Console()
        
        ecc = ((r_a-r_p)/(r_a+r_p)) #calculating the eccentricity using the apsides...

        if ecc==0:
            console.print('\n[bold yellow]Perfect circle[/bold yellow]\n')
        elif 0<ecc<1:
            console.print('\n[bold yellow]Ellipse (bound orbit)[/bold yellow]\n')
        elif ecc==1:
            console.print('\n[bold yellow]Parabola (escape orbit)[/bold yellow]\n')
        elif ecc>1:
            console.print('\n[bold yellow]Hyperbola (unbound orbit)[/bold yellow]\n')

        major_axis = (r_a+r_p)
        semi_major_axis = (major_axis/2) if major_axis else ((r_a+r_p)/2)



        if tble:
            table=Table(title='...SOLAR SYSTEM...')

            table.add_column('Object',style='Cyan')
            table.add_column('Perihelion\n*rp**AU*',style='magenta')
            table.add_column('Aphelion\n*ra**AU*',style='Cyan')
            table.add_column('Semi-major axis\n*AU*',style='magenta')
            table.add_column('Orbital\neccentricity',style='Cyan')

            table.add_row('Mercury',f'{self.Mercury_rP}',f'{self.Mercury_rA}',f'{self.Mercury_AU}',f'{self.Mercury_e}')
            table.add_row('Venus',f'{self.Venus_rP}',f'{self.Venus_rA}',f'{self.Venus_AU}',f'{self.Venus_e}')
            table.add_row('Earth',f'{self.Earth_rP}',f'{self.Earth_rA}',f'{self.Earth_AU}',f'{self.Earth_e}')
            table.add_row('Mars',f'{self.Mars_rP}',f'{self.Mars_rA}',f'{self.Mars_AU}',f'{self.Mars_e}')
            table.add_row('Ceres',f'{self.Ceres_rP}',f'{self.Ceres_rA}',f'{self.Ceres_AU}',f'{self.Ceres_e}')
            table.add_row('Jupiter',f'{self.Jupiter_rP}',f'{self.Jupiter_rA}',f'{self.Jupiter_AU}',f'{self.Jupiter_e}')
            table.add_row('Saturn',f'{self.Saturn_rP}',f'{self.Saturn_rA}',f'{self.Saturn_AU}',f'{self.Saturn_e}')
            table.add_row('Uranus',f'{self.Uranus_rP}',f'{self.Uranus_rA}',f'{self.Uranus_AU}',f'{self.Uranus_e}')
            table.add_row('Neptune',f'{self.Neptune_rP}',f'{self.Neptune_rA}',f'{self.Neptune_AU}',f'{self.Neptune_e}')
            table.add_row('Pluto',f'{self.Pluto_rP}',f'{self.Pluto_rA}',f'{self.Pluto_AU}',f'{self.Pluto_e}')
            table.add_row('Haumea',f'{self.Haumea_rP}',f'{self.Haumea_rA}',f'{self.Haumea_AU}',f'{self.Haumea_e}')
            table.add_row('Makemake',f'{self.Makemake_rP}',f'{self.Makemake_rA}',f'{self.Makemake_AU}',f'{self.Makemake_e}')
            table.add_row('Eris',f'{self.Eris_rP}',f'{self.Eris_rA}',f'{self.Eris_AU}',f'{self.Eris_e}')
            console.print(table)
            print()
            console.print(f'[bold green]\n..Average distance of Earth from sun: {self.AU_m} (m)[/bold green]')
            



        print(f'\neccentricity: {round(ecc,3)}\nMajor axis: {round(major_axis,3)}\nSemi major axis: {round(semi_major_axis,3)}\n')


        #print('listing of function arguments respectively:\n(harmonic fxn): 1.velocity 2.distance btwn the two objects/masses 3.mass 4.Mass')


@click.group()
#@click.option(help='in some calculations, only one mass is required.you can use either of the --mass/--Mass options.In other calculations both the masses are required therefore use the two options --mass/--Mass respectively')
@click.option('--tble',default=None,help='if not None, a table containing values of the solar system will be printed to the console')
@click.pass_context
def term(ctx,tble):
    ctx.obj=Astro(tble)

@term.command()
@click.option('--velocity',default=1,help='the velocity of the object in space. Use the SI unit m/s',type=float)
@click.option('--distance',default=1,help='the distance between the two objects in space. Use the SI unit m',type=float)
@click.option('--mass',default=1,help='the Mass of the smaller mass. Use the SI unit kg',type=float)
@click.option('--ass',default=1,help='the Mass of the larger mass. Use the SI unit kg',type=float)
@click.option('--o_p',default=1,help='the orbital period of the planet if known.',type=float)
@click.pass_obj
def harmonic(astro,velocity,distance,mass,ass,o_p):
    astro.harmonic(velocity,distance,mass,ass,o_p)


@term.command()
@click.option('--r_a',default=1,help='apside value (aphelion) which is the maximum distance from the sun',type=float)
@click.option('--r_p',default=1,help='apside value (perihelion) which is the minimum distance from the sun',type=float)
@click.option('--tble',default=None,help='if not None, a table containing values of the solar system will be printed to the console')
@click.pass_obj
def eccent(astro,r_a,r_p,tble):
    astro.eccent(r_a,r_p,tble)
    if tble:
        astro.tebl()


@term.command()
@click.option('--k_e',default=1,help='kinetic energy value',type=float)
@click.option('--p_e',default=1,help='potential energy value',type=float)
@click.option('--distance',default=1,help='distance between the two object or masses',type=float)
@click.option('--mass',default=1,help='the mass of the smaller mass',type=float)
@click.option('--ass',default=1,help='the mass of the larger Mass',type=float)
@click.option('--tble',default=None,help='if not None, a table containing values will be printed to the console')
@click.pass_obj
def energy(astro,k_e,p_e,mass,ass,distance,tble):
    astro.energy(k_e,p_e,mass,ass,distance,tble)
    if tble:
        astro.tebl()


@term.command()
@click.option('--proper_time',default=1,help='for the stationary object at or near the surface of the mass',type=float)
@click.option('--coordinate_time',default=1,help='for the distant stationary object where space time is flat',type=float)
@click.option('--mass',default=1,help='the mass of the Mass',type=float)
@click.option('--distance',default=1,help='the distance from the center of the Mass to the stationary object at or near the surface of the mass',type=float)
@click.pass_obj
def timee(astro,mass,distance,coordinate_time,proper_time):
    astro.timee(mass,distance,coordinate_time,proper_time)



@term.command()
@click.option('--parallax',default=1,help='the value of the parallax angle',type=float)
@click.option('--distance',default=1,help='the distance in meters if it is the only value available',type=float)
@click.option('--light_years',default=1,help='the value of light years if it is the only value available',type=float)
@click.pass_obj
def distance(astro,parallax,distance,light_years):
    astro.distance(parallax,distance,light_years)

@term.command()
@click.option('--days_elapsed',default=0,help='the number of days elapsed since the epoch',type=int)
@click.option('--period',default=-1,help='the period in days for the planet. Use int as the number type',type=int)
@click.option('--planet',default=None,help='the object value 1 for Mercury\n2 for Venus\n3 for Earth\n4 for Mars\n5 for Ceres \n6 for Jupiter\n7 for Saturn\n8 for Uranus\n9 for Neptune\n10 for Pluto\n11 for Eris.',type=int)
@click.option('--eccentric',default=None,help='inputing this will activate eccentric orbits')
@click.pass_obj
def orbit(astro,days_elapsed,period,planet,eccentric):
    astro.orbit(days_elapsed,period,planet,eccentric)


if __name__ == '__main__':                                          term()
