Feature: Scan Workflow

  Scenario: User initiates a scan and views results
    Given the user is on the Pdatatrigger frontend
    When the user enters "http://example.com" in the target URL field
    And the user clicks the "Scan" button
    Then the user should see the scan results for "http://example.com"
    And the user should see a list of vulnerabilities

    