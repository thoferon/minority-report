{ pkgs }:

let
  pythonVersion = "python38";

  pyPkgs = pkgs."${pythonVersion}Packages";

  inherit (pyPkgs) buildPythonPackage;

  python = pkgs.${pythonVersion}.withPackages (p: with p; [
    influxdb
    pandas
    pylint
  ]);

in
[
  python
]
