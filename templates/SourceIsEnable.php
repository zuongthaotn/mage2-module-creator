<?php
namespace {{namespace}}\{{module_name}}\Model\{{interface_name}}\Source;

use Magento\Framework\Data\OptionSourceInterface;

/**
 * Class IsEnable
 */
class IsEnable implements OptionSourceInterface
{
    /**
     * @var \{{namespace}}\{{module_name}}\Model\{{interface_name}}
     */
    protected ${{interface_name_lower}};

    /**
     * Constructor
     *
     * @param \{{namespace}}\{{module_name}}\Model\{{interface_name}} ${{interface_name_lower}}
     */
    public function __construct(\{{namespace}}\{{module_name}}\Model\{{interface_name}} ${{interface_name_lower}})
    {
        $this->{{interface_name_lower}} = ${{interface_name_lower}};
    }

    /**
     * Get options
     *
     * @return array
     */
    public function toOptionArray()
    {
        $availableOptions = $this->{{interface_name_lower}}->getAvailableStatuses();
        $options = [];
        foreach ($availableOptions as $key => $value) {
            $options[] = [
                'label' => $value,
                'value' => $key,
            ];
        }
        return $options;
    }
}
