#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import basic_meta_pb2 as basic__meta__pb2
import proxy_pb2 as proxy__pb2


class DataTransferServiceStub(object):
  """data transfer service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.push = channel.stream_unary(
        '/com.webank.ai.fate.api.networking.proxy.DataTransferService/push',
        request_serializer=proxy__pb2.Packet.SerializeToString,
        response_deserializer=proxy__pb2.Metadata.FromString,
        )
    self.pull = channel.unary_stream(
        '/com.webank.ai.fate.api.networking.proxy.DataTransferService/pull',
        request_serializer=proxy__pb2.Metadata.SerializeToString,
        response_deserializer=proxy__pb2.Packet.FromString,
        )
    self.unaryCall = channel.unary_unary(
        '/com.webank.ai.fate.api.networking.proxy.DataTransferService/unaryCall',
        request_serializer=proxy__pb2.Packet.SerializeToString,
        response_deserializer=proxy__pb2.Packet.FromString,
        )


class DataTransferServiceServicer(object):
  """data transfer service
  """

  def push(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def pull(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def unaryCall(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataTransferServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'push': grpc.stream_unary_rpc_method_handler(
          servicer.push,
          request_deserializer=proxy__pb2.Packet.FromString,
          response_serializer=proxy__pb2.Metadata.SerializeToString,
      ),
      'pull': grpc.unary_stream_rpc_method_handler(
          servicer.pull,
          request_deserializer=proxy__pb2.Metadata.FromString,
          response_serializer=proxy__pb2.Packet.SerializeToString,
      ),
      'unaryCall': grpc.unary_unary_rpc_method_handler(
          servicer.unaryCall,
          request_deserializer=proxy__pb2.Packet.FromString,
          response_serializer=proxy__pb2.Packet.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.fate.api.networking.proxy.DataTransferService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class RouteServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.query = channel.unary_unary(
        '/com.webank.ai.fate.api.networking.proxy.RouteService/query',
        request_serializer=proxy__pb2.Topic.SerializeToString,
        response_deserializer=basic__meta__pb2.Endpoint.FromString,
        )


class RouteServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RouteServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'query': grpc.unary_unary_rpc_method_handler(
          servicer.query,
          request_deserializer=proxy__pb2.Topic.FromString,
          response_serializer=basic__meta__pb2.Endpoint.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.fate.api.networking.proxy.RouteService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TaskAdminServiceStub(object):
  """task administration service. will change in phase 2 / 3
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.start = channel.unary_unary(
        '/com.webank.ai.fate.api.networking.proxy.TaskAdminService/start',
        request_serializer=proxy__pb2.Metadata.SerializeToString,
        response_deserializer=proxy__pb2.Metadata.FromString,
        )
    self.stop = channel.unary_unary(
        '/com.webank.ai.fate.api.networking.proxy.TaskAdminService/stop',
        request_serializer=proxy__pb2.Metadata.SerializeToString,
        response_deserializer=proxy__pb2.Metadata.FromString,
        )
    self.kill = channel.unary_unary(
        '/com.webank.ai.fate.api.networking.proxy.TaskAdminService/kill',
        request_serializer=proxy__pb2.Metadata.SerializeToString,
        response_deserializer=proxy__pb2.Metadata.FromString,
        )
    self.heartbeat = channel.unary_unary(
        '/com.webank.ai.fate.api.networking.proxy.TaskAdminService/heartbeat',
        request_serializer=proxy__pb2.Metadata.SerializeToString,
        response_deserializer=proxy__pb2.HeartbeatResponse.FromString,
        )


class TaskAdminServiceServicer(object):
  """task administration service. will change in phase 2 / 3
  """

  def start(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def kill(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def heartbeat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TaskAdminServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'start': grpc.unary_unary_rpc_method_handler(
          servicer.start,
          request_deserializer=proxy__pb2.Metadata.FromString,
          response_serializer=proxy__pb2.Metadata.SerializeToString,
      ),
      'stop': grpc.unary_unary_rpc_method_handler(
          servicer.stop,
          request_deserializer=proxy__pb2.Metadata.FromString,
          response_serializer=proxy__pb2.Metadata.SerializeToString,
      ),
      'kill': grpc.unary_unary_rpc_method_handler(
          servicer.kill,
          request_deserializer=proxy__pb2.Metadata.FromString,
          response_serializer=proxy__pb2.Metadata.SerializeToString,
      ),
      'heartbeat': grpc.unary_unary_rpc_method_handler(
          servicer.heartbeat,
          request_deserializer=proxy__pb2.Metadata.FromString,
          response_serializer=proxy__pb2.HeartbeatResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.fate.api.networking.proxy.TaskAdminService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
