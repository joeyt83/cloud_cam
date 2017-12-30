#!/usr/bin/env python
import unittest
from mock import patch, Mock
from cloud_cam import CloudCamClient

def return_code(code):
  xml = """
  <?xml version="1.0" encoding="UTF-8"?>
  <ResponseStatus version="1.0" xmlns="urn:psialliance-org">
  <requestURL>/PSIA/PTZ/channels/1/continuous</requestURL>
  <statusCode>%s</statusCode>
  <statusString>OK</statusString>
  </ResponseStatus>
  """
  resp = xml % code
  return resp.strip()

def make_standard_assertions(req):
  assert req.get_full_url()=='http://cloudcam_host/PSIA/PTZ/channels/1/continuous'
  assert len(req.headers)==1 and req.headers['Authorization'].startswith('Basic')
  assert req.get_method()=='PUT'

class CloudCamTest(unittest.TestCase):

  def setUp(self):
    self.client = CloudCamClient("cloudcam_host", "uza", "pwd")
    self.mock_opener = Mock()
    self.mock_opened_request = Mock()
    self.mock_opener.open.return_value = self.mock_opened_request

  @patch('urllib2.build_opener')
  def testZoomIn(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(1)

    self.client.zoom_in()

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)

    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><zoom>2</zoom></PTZData>' 
  
  @patch('urllib2.build_opener')
  def testZoomOut(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(1)

    self.client.zoom_out()

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)
    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><zoom>-2</zoom></PTZData>' 
  
  @patch('urllib2.build_opener')
  def testTiltUp(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(1)

    self.client.tilt_up()

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)
    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><tilt>2</tilt></PTZData>' 
  
  @patch('urllib2.build_opener')
  def testTiltDown(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(1)

    self.client.tilt_down()

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)
    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><tilt>-2</tilt></PTZData>' 
  
  @patch('urllib2.build_opener')
  def testPanLeft(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(1)

    self.client.pan_left()

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)
    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><pan>2</pan></PTZData>' 
  
  @patch('urllib2.build_opener')
  def testPanRight(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(1)

    self.client.pan_right()

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)
    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><pan>-2</pan></PTZData>' 
  
  @patch('urllib2.build_opener')
  def testFreeze(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(1)

    self.client.freeze()

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)
    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><pan>0</pan><tilt>0</tilt><zoom>0</zoom></PTZData>' 
  
  @patch('urllib2.build_opener')
  def testZoomError(self, mock_build_opener):
    mock_build_opener.return_value = self.mock_opener
    self.mock_opened_request.read.return_value = return_code(2)
  
    try:
      self.client.zoom_in()
      raise Exception("Expected to fail but didn't.")
    except AssertionError:
      pass

    req = self.mock_opener.open.call_args[0][0]
    make_standard_assertions(req)
    assert req.data=='<?xml version:"1.0" encoding="UTF-8"?><PTZData><zoom>2</zoom></PTZData>' 
  

if __name__ == '__main__':
  unittest.main()
