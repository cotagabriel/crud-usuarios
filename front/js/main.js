var App = angular.module('App', ['ngRoute', 'ui.mask']);

App.config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider){
  $httpProvider.defaults.useXDomain = true;
  delete $httpProvider.defaults.headers.common['X-Requested-With'];

  $routeProvider.when('/', {
    controller: 'UsuarioController',
    templateUrl: 'index.html'
  })
  .when('/usuarios', {
    controller: 'UsuarioController',
    templateUrl: 'index.html'
  })
  .when('/usuarios/adicionar', {
    controller: 'UsuarioController',
    templateUrl: 'index.html'
  })
  .when('/usuarios/alterar/:id', {
    controller: 'UsuarioController',
    templateUrl: 'index.html'
  })
  .when('/usuarios/remover/:id', {
    controller: 'UsuarioController',
    templateUrl: 'index.html'
  })
  .otherwise({
    redirectTo: '/'
  });
}]);
