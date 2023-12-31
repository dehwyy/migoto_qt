# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: src/proto/auth.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from internal.lib.twirp_client import TwirpClient

_sym_db = _symbol_database.Default()

class AuthRPCServer(TwirpServer):

	def __init__(self, *args, service, server_path_prefix="/twirp"):
		super().__init__(service=service)
		self._prefix = F"{server_path_prefix}/auth.AuthRPC"
		self._endpoints = {
			"SignUp": Endpoint(
				service_name="AuthRPC",
				name="SignUp",
				function=getattr(service, "SignUp"),
				input=_sym_db.GetSymbol("auth.SignUpRequest"),
				output=_sym_db.GetSymbol("auth.AuthResponse"),
			),
			"SignIn": Endpoint(
				service_name="AuthRPC",
				name="SignIn",
				function=getattr(service, "SignIn"),
				input=_sym_db.GetSymbol("auth.SignInRequest"),
				output=_sym_db.GetSymbol("auth.AuthResponse"),
			),
			"IsUniqueUsername": Endpoint(
				service_name="AuthRPC",
				name="IsUniqueUsername",
				function=getattr(service, "IsUniqueUsername"),
				input=_sym_db.GetSymbol("auth.IsUniqueUsernamePayload"),
				output=_sym_db.GetSymbol("auth.IsUnique"),
			),
			"VerifyUserEmail": Endpoint(
				service_name="AuthRPC",
				name="VerifyUserEmail",
				function=getattr(service, "VerifyUserEmail"),
				input=_sym_db.GetSymbol("general.UserId"),
				output=_sym_db.GetSymbol("general.IsSuccess"),
			),
			"ChangePassword": Endpoint(
				service_name="AuthRPC",
				name="ChangePassword",
				function=getattr(service, "ChangePassword"),
				input=_sym_db.GetSymbol("auth.ChangePasswordPayload"),
				output=_sym_db.GetSymbol("general.IsSuccess"),
			),
			"Logout": Endpoint(
				service_name="AuthRPC",
				name="Logout",
				function=getattr(service, "Logout"),
				input=_sym_db.GetSymbol("general.UserId"),
				output=_sym_db.GetSymbol("general.IsSuccess"),
			),
		}

class AuthRPCClient(TwirpClient):

	def SignUp(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/auth.AuthRPC/SignUp",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("auth.AuthResponse"),
			**kwargs,
		)

	def SignIn(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/auth.AuthRPC/SignIn",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("auth.AuthResponse"),
			**kwargs,
		)

	def IsUniqueUsername(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/auth.AuthRPC/IsUniqueUsername",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("auth.IsUnique"),
			**kwargs,
		)

	def VerifyUserEmail(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/auth.AuthRPC/VerifyUserEmail",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("general.IsSuccess"),
			**kwargs,
		)

	def ChangePassword(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/auth.AuthRPC/ChangePassword",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("general.IsSuccess"),
			**kwargs,
		)

	def Logout(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/auth.AuthRPC/Logout",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("general.IsSuccess"),
			**kwargs,
		)
