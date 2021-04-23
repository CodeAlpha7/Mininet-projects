""" Testing custom topology writing for mininet and ryu controller

use ryu controller for this topology.
ryu-manager ryu.app.simple_switch_13
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class customtopo(Topo):
	
	def build(self):
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2)
		"add all switches here"
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		"add all hosts here"
		"can also specify mac and ip"
		
		self.addLink(h1, s1)
		self.addLink(h2, s2)
		"make all links here"
		
if __name__ == '__main__':
	setLogLevel('info')
	topo = customtopo()
	"Now set the controller"
	c1 = RemoteController('c1', ip='127.0.0.1')
	net = Mininet(topo=topo, controller=c1)
	net.start()
	net.pingAll() 
	"this pings all hosts as soon as topology is set"
	"can also remove this"
	CLI(net)
	net.stop()
	
