Feature: Test CRUD methods in Snippets REST API testing framework

Background:
    Given I set snippets REST API url
    
Scenario: POST/CREATE snippet example
	Given I set POST snippet api endpoint
	When I set auth_header param username as "app_user1"
	And I set auth_header param password as "app_user1"
    And I set request Body
 	And I send a POST HTTP request
 	Then I receive valid HTTP response code 201 for POST
 	And Response BODY POST is non-empty

Scenario: GET snippet example
  	Given I set GET snippet api endpoint with id of snippet created in POST scenario
    When I send GET HTTP request
  	Then I receive valid HTTP response code 200 for "GET" 
    And Response BODY "GET" is non-empty

Scenario: PUT/UPDATE snippet example with id of snippet created in POST scenario
  	Given I set PUT snippet api endpoint with id of snippet created in POST scenario
    When I set request Body for PUT
 	And I send a PUT HTTP request with the same credentials as in POST scenario
 	Then I receive valid HTTP response code 200 for PUT
 	And Response BODY PUT is non-empty
 	
Scenario: PUT/UPDATE snippet example with unauthorized user app_user2/app_user2
 	When I send a PUT HTTP request with snippet id created in POST scenario for unauthorized user app_user2/app_user2
 	Then I receive valid error message PUT for unauthorized user
 	
Scenario: DELETE snippet example with id of snippet created in POST scenario
 	When I send a DELETE HTTP request with snippet id created in POST scenario
 	Then I receive valid http code 204 No Content

 	