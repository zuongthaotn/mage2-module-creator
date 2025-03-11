<?php

namespace {{namespace}}\{{module_name}}\Api\Data;

/**
 * {{interface_name}} interface.
 * @api
 * @since 100.0.2
 */
interface {{interface_name}}Interface
{
    /**#@+
     * Constants for keys of data array. Identical to the name of the getter in snake case
     */
    const {{interface_name_upper}}_ID       = '{{interface_name_lower}}_id';
    const NAME              = 'name';
    const IS_ENABLE         = 'is_enable';
    /**#@-*/

    /**#@+
     * {{interface_name}}'s statuses
     */
    const STATUS_ENABLED = 1;

    const STATUS_DISABLED = 0;

    /**
     * Get ID
     *
     * @return int|null
     */
    public function getId();

    /**
     * Get title
     *
     * @return string
     */
    public function getName();

    /**
     * Is enable
     *
     * @return bool|null
     */
    public function isEnable();

    /**
     * Set ID
     *
     * @param int $id
     * @return {{interface_name}}Interface
     */
    public function setId($id);

    /**
     * Set name
     *
     * @param string $name
     * @return {{interface_name}}Interface
     */
    public function setName($name);

    /**
     * Set is enable
     *
     * @param bool|int $isEnable
     * @return {{interface_name}}Interface
     */
    public function setIsEnable($isEnable);
}
