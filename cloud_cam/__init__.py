import urllib2
import base64
import xml.etree.ElementTree

class CloudCamClient():

  def __init__(self, host, username, password, move_speed):
    self.host = host
    self.username = username
    self.password = password
    self.move_speed = move_speed

  def send_ptz_request(self, ptz_xml):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    url='http://%s/PSIA/PTZ/channels/1/continuous' % self.host
    xml_data="<?xml version:\"1.0\" encoding=\"UTF-8\"?><PTZData>%s</PTZData>" % (ptz_xml)
    request = urllib2.Request(url, xml_data)
    base64string = base64.encodestring('%s:%s' % (self.username, self.password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string) 
    request.get_method = lambda: 'PUT'
    resp_xml = opener.open(request).read()
    e = xml.etree.ElementTree.fromstring(resp_xml)
    resp_code = e.getchildren()[1].text
    assert resp_code == '1'

  def send_zoom_request(self, speed):
    self.send_ptz_request("<zoom>%s</zoom>" % speed)

  def send_tilt_request(self, speed):
    self.send_ptz_request("<tilt>%s</tilt>" % speed)

  def send_pan_request(self, speed):
    self.send_ptz_request("<pan>%s</pan>" % speed)

  def zoom_in(self):
    self.send_zoom_request(self.move_speed)

  def zoom_out(self):
    self.send_zoom_request(-self.move_speed)

  def tilt_up(self):
    self.send_tilt_request(-self.move_speed)

  def tilt_down(self):
    self.send_tilt_request(self.move_speed)

  def pan_left(self):
    self.send_pan_request(self.move_speed)

  def pan_right(self):
    self.send_pan_request(-self.move_speed)

  def freeze(self):
    self.send_ptz_request("<pan>0</pan><tilt>0</tilt><zoom>0</zoom>")
