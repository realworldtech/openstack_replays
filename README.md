# Openstack Replays

Toolset for restoring openstack volumes via replays when using Openstack Cinder in conjunction with a Dell SMC solution.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Docker >= 17
Docker-compose >= 1.20.0
```

### Installing

Build the app
```
docker-compose build
```

Once built execute the run file:
```
# ./run.sh
```

## Running the tests

There is currently no tests to run.


## Built With

- [Openstack SDK](https://docs.openstack.org/openstacksdk/) Python SDK for Openstack as a whole.
- [InfiniDat Munch](https://github.com/Infinidat/munch) "Munch" is a Python dictionary that provides attribute-style access (a la JavaScript objects).
- [NPYScreen](http://npyscreen.readthedocs.io/) for my UI

Elements of the connectivity to SC Storage Arrays have been ported from the Dell Base Flocker Driver. (Note that this project is originally distributed under the Apache 2.0 Open Source License)
- [Dell Base Flock Driver](https://github.com/dellstorage/storagecenter-flocker-driver)

## Contributing

Fork, modify and submit a pull request. Simple.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.realworld.net.au/realworldtech/openstack_replays/tags).

## Authors

* **Karl Kloppenborg** - *Initial work* - [inventionlabsSydney](https://github.com/inventionlabsSydney)
* **Andrew Yager** - *Documentation and some cleanup* - [andrewyager](https://github.com/andrewyager)

See also the list of [contributors](https://github.realworld.net.au/realworldtech/openstack_replays/contributors) who participated in this project.

## License

This project is licensed under the MIT License.

## Acknowledgments

* Dell Storage Solutions for base api code.
* Andrew Yager [andrewyager](https://github.com/andrewyager) for discovering the createView and list_replays requirements I needed)

--Karl
